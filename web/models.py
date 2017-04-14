# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Registration(models.Model):
    firstname = models.CharField(u'Имя', max_length=32)
    lastname = models.CharField(u'Фамилия', max_length=32)
    comment = models.TextField(u'Комментарий', max_length=1000)
    is_submit = models.BooleanField(u'Подтверждено', default=False)


class Hotel(models.Model):
    firstname = models.CharField(u'Имя', max_length=32)
    lastname = models.CharField(u'Фамилия', max_length=32)
    comment = models.TextField(u'Комментарий', max_length=1000)
    is_submit = models.BooleanField(u'Подтверждено', default=False)
