# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('check_interval', models.IntegerField(default=60)),
                ('status', models.CharField(max_length=20)),
                ('last_checked', models.DateTimeField()),
                ('max_confirmations', models.IntegerField(default=3)),
                ('confirmations', models.IntegerField()),
                ('lock', models.CharField(max_length=16)),
                ('last_locked', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CheckAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('check_id', models.ForeignKey(to='checks.Check')),
            ],
        ),
        migrations.CreateModel(
            name='CheckType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CheckTypeAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField()),
                ('attribute_type', models.CharField(max_length=255)),
                ('check_type', models.ForeignKey(to='checks.CheckType')),
            ],
        ),
        migrations.AddField(
            model_name='checkattribute',
            name='check_type_attribute',
            field=models.ForeignKey(to='checks.CheckTypeAttribute'),
        ),
        migrations.AddField(
            model_name='check',
            name='check_type',
            field=models.ForeignKey(to='checks.CheckType'),
        ),
        migrations.AddField(
            model_name='check',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
