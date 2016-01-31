# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0002_auto_20160131_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='confirmations',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='last_checked',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='last_locked',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='lock',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='status',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
