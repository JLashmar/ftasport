# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20171108_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='headline_image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
