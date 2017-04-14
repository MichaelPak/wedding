# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32, verbose_name='\u0418\u043c\u044f')),
                ('lastname', models.CharField(max_length=32, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('comment', models.TextField(max_length=1000, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('is_submit', models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e')),
            ],
        ),
    ]