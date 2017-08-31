# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-31 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.PositiveSmallIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.PositiveSmallIntegerField(blank=True, default=1, null=True),
        ),
    ]
