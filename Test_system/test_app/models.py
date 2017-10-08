from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Имя, Фамилия", max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return (self.name)


class Group(models.Model):
    group = models.CharField("Название группы", blank=True, max_length=1000000)
    users = models.ManyToManyField(User, default='',blank=True)


    def __str__(self):
        return (self.group)


class Test(models.Model):

    test_description = models.CharField("Описание теста",unique=True,max_length=1000)
    groups = models.ManyToManyField(Group, default='',blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def __str__(self):
        return (self.test_description)


class Message(models.Model):
    text = models.CharField("Текст сообщения",max_length=100)
    groups = models.ManyToManyField(Group, default='', blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.text

class Applications(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(User, default='',blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return (self.id)

class Review(models.Model):
    tests = models.ForeignKey(Test, on_delete=models.CASCADE, default='')
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.group
