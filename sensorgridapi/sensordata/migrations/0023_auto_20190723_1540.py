# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-23 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0022_auto_20180514_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField()),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensordata.Network')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together=set([('node_id', 'network')]),
        ),
    ]
