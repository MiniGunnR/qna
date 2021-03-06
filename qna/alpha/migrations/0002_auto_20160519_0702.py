# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 07:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationObjectActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notificationdetail',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='notificationdetail',
            name='obj',
        ),
        migrations.RemoveField(
            model_name='notificationdetail',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='notificationobject',
            unique_together=set([]),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='NotificationDetail',
        ),
        migrations.AddField(
            model_name='notificationobjectactor',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alpha.NotificationObject'),
        ),
        migrations.RemoveField(
            model_name='notificationobject',
            name='action',
        ),
        migrations.RemoveField(
            model_name='notificationobject',
            name='url',
        ),
    ]
