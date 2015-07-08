# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150706_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='residence',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(blank=True, max_length=50, choices=[(b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019')]),
        ),
    ]
