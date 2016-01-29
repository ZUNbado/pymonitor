# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkattribute',
            name='check_type_attribute',
            field=models.ForeignKey(to='checks.CheckTypeAttribute'),
        ),
    ]
