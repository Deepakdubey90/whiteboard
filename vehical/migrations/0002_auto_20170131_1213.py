# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicalparking',
            name='vehical_intime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='vehicalparking',
            name='vehical_outtime',
            field=models.TimeField(),
        ),
    ]
