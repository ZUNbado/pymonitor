# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='confirmations',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='last_checked',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='last_locked',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='lock',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='status',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
