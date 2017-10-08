"""Test_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from test_app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.begin_page, name='begin_page'),
    url(r'^test_list/$', views.new_test, name='new_test'),
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^create_group/$', views.create_group, name='create_group'),
    url(r'^new_user/$', views.create_user, name='create_user'),
    url(r'^group_list/$', views.group_list, name='group_list'),
    url(r'^send_message/$', views.send_message, name='send_message'),
    url(r'^review/$', views.create_review, name='create_review'),
    url(r'^stac/$', views.send_file, name='send_file'),
    #url(r'^new_group/$', views.new_group, name='new_group'),

    #url(r'^group_list/$', views.group_list, name='group_list'),

]
