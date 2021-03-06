# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-14 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20190714_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='hostname',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='vm_status',
            field=models.IntegerField(choices=[(0, '在线'), (1, '下线'), (2, '空闲中')], verbose_name='服务器状态'),
        ),
    ]
