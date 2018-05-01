# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 10:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocxdonado', '0003_auto_20180426_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propono',
            name='nombro_eblaj_elektoj',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='nombro da eblaj elektoj'),
        ),
    ]
