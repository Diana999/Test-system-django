# -*- coding: utf-8 -*-
import html.parser, requests
import time
from django.utils import timezone
from .forms import TestForm, UserForm, GroupForm, MessageForm, ReviewForm
from django.contrib import messages
from .models import User, Test, Group, Message, Review, Applications
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.conf import settings
import mimetypes
import glob
from dominate import document
from dominate.tags import *

def begin_page(request):
    return render(request, 'test_app/begin_page.html', {})


def user_list(request):
    users  = User.objects.all()
    dict = {'users':users}
    return render(request, 'test_app/user_list.html', dict)


def group_list(request):
    groups = Group.objects.all()
    dict = {
        'groups':groups,
    }
    return render(request, 'test_app/group_list.html', dict)


def new_test(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        tag = form.cleaned_data['groups']
        for tag_name in tag:
            instance.groups.add(tag_name)
        messages.success(request, "Новый тест создан")
        return redirect("begin_page")
    else:
        test = Test.objects.all()
        return render(request, 'test_app/test_page.html', {'form': form, 'test':test})


def create_group(request):
    users  = User.objects.all()
    form = GroupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        tag = form.cleaned_data['users']
        for tag_name in tag:
            instance.users.add(tag_name)
        messages.success(request, "Новая группа создан")
        return redirect("begin_page")

    dict = {'users':users, 'form':form}
    return render(request, 'test_app/create_group.html', dict)


def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "User successfully Created")
        return redirect("user_list")
    else:
        return render(request, 'test_app/create_user.html', {'form': form})


def send_message(request):
    form  = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        tag = form.cleaned_data['groups']
        for tag_name in tag:
            instance.groups.add(tag_name)
        messages.success(request, "Message delivered")
        return redirect("begin_page")
    else:
        return render(request, 'test_app/send_message.html', {'form':form})


def create_review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

        messages.success(request, "Отчет сгенерирован")
        return redirect("send_file")
    else:
        return render(request, 'test_app/choose_test.html', {'form': form})

def create_html():
    review = Review.objects.latest("published_date")  # сам последний объект
    test = review.tests.test_description  # Название теста последнего отзыва
    # Теперь узнать, какие группы принимали участие в тесте
    groups = review.tests.groups.all()  # список групп теста в виде листа
    num_groups = review.tests.groups.count()  # количество этих групп
    group_objects_all = Group.objects.all()  # Это нужно, чтобы узнать пользователей в группе, их колиечство и заявки
    group_objects = []
    for i in review.tests.groups.all():
        for j in group_objects_all:
            if i == j:
                group_objects.append(j)
    # Теперь в груп обжектс хранятся экземпляры класса группы, через которые мы можем посчитать пользователей
    # Перед этим нужно сохранить этих пользоваталей и апликашоны
    users = []
    for u in group_objects:
        for us in u.users.all():
            users.append(us)
    users = set(users)  # Здесь у нас хранятся индивидуальные пользователи
    counter = 0
    for i in users:
        for j in Applications.objects.all():
            if i in j.user_id.all():
                counter += 1
    # каунтер это количество заявок от них
    real_dic = {
        'review': review,
        'test': test,
        'groups': groups,
        'num_groups': num_groups,
        'nums': counter,
        'users': users
    }

    with document(title=test) as doc:
        h1("Name of the test")
        h1(test)
        h3("Number of groups in ")
        h3(num_groups)

        for g in groups:
            h3(str(g))
        h3("Number of users in groups")
        h3(len(users))
        h3("Number of applications in group")
        h3(counter)

    with open('gallery.html', 'w') as f:
        f.write(doc.render())


def send_file(request):
    create_html()
    filename     = "/Users/dianagajnutdinova/Codes/Python/Work_Test_project/Test_system/gallery.html" # Select your file here.
    download_name ="review.html"
    wrapper      = FileWrapper(open(filename))
    content_type = 'html'
    response     = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response


