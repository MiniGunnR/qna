# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alpha', '0003_auto_20160519_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('primary_actor', models.CharField(default='Someone', max_length=50)),
                ('actor_count', models.PositiveIntegerField(default=0)),
                ('action', models.CharField(default='wrote an answer to your question.', max_length=200)),
                ('url', models.URLField()),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationObjectActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alpha.NotificationObject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='notificationobject',
            unique_together=set([('user', 'action', 'url')]),
        ),
    ]
