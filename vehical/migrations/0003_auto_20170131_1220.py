# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehical', '0002_auto_20170131_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicalparking',
            name='vehical_type',
            field=models.CharField(default=b'cycle', max_length=30, choices=[(b'truck', b'TRUCK'), (b'suv', b'SUV'), (b'car', b'CAR'), (b'byke', b'BYKE'), (b'cycle', b'CYCLE')]),
        ),
    ]
