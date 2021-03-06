# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_auto_20170310_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='orgabbrname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgimageurl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgjurisdictiontype',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgparentid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgtype',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgurladdress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgurltext',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
