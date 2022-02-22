# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:09
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='claimed_projects',
            field=models.ManyToManyField(default='', related_name='claimed_projects', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='known_skills',
            field=models.ManyToManyField(default='', related_name='known', to='profiles.Skills'),
        ),
        migrations.AddField(
            model_name='profile',
            name='learn_skills',
            field=models.ManyToManyField(default='', related_name='learn', to='profiles.Skills'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alert',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alert',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL),
        ),
    ]
