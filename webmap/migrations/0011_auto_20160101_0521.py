# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 05:21
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webmap', '0010_auto_20151231_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_create', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
        migrations.AlterField(
            model_name='poi',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poi_create', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='poi',
            name='geom_multi',
            field=django.contrib.gis.db.models.fields.GeometryCollectionField(help_text='Add point: Select pencil with plus sign icon and place your point to the map.<br/>\n            Add line: Select line icon and by clicking to map draw the line. Finish drawing with double click.<br/>\n            Add area: Select area icon and by clicking to mapy draw the area. Finish drawing with double click.<br/>\n            Object edition: Select the first icon and then select object in map. Draw points in map to move them, use points in the middle of sections to add new edges.', srid=4326, verbose_name='place geometry', null=True),
        ),
        migrations.AlterField(
            model_name='poi',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poi_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
    ]
