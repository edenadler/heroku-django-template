# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-19 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard_app', '0003_auto_20170219_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
