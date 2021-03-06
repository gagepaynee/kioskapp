# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_competition_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='picture',
            field=models.ImageField(default='gearbg.png', upload_to='clubs'),
        ),
        migrations.AddField(
            model_name='major',
            name='picture',
            field=models.ImageField(default='gearbg.png', upload_to='majors'),
        ),
        migrations.AddField(
            model_name='ourstory',
            name='picture',
            field=models.ImageField(default='gearbg.png', upload_to='ourstory'),
        ),
    ]
