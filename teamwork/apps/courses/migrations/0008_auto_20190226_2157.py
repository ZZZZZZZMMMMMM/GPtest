# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190123_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to='csv_files/'),
        ),
    ]
