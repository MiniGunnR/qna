# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0002_auto_20160519_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationobjectactor',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='notificationobjectactor',
            name='obj',
        ),
        migrations.DeleteModel(
            name='NotificationObject',
        ),
        migrations.DeleteModel(
            name='NotificationObjectActor',
        ),
    ]
