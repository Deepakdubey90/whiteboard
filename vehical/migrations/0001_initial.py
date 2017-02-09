# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicalParking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehical_name', models.CharField(max_length=30)),
                ('vehical_number', models.CharField(max_length=50)),
                ('vehical_type', models.CharField(default=b'cycle', max_length=30, choices=[(b'truck', b'TRUCK'), (b'suv', b'SUV'), (b'car', b'CAR'), (b'bike', b'BYKE'), (b'cycle', b'CYCLE')])),
                ('vehical_intime', models.DateTimeField()),
                ('vehical_outtime', models.DateTimeField()),
                ('park_fare', models.CharField(max_length=100)),
            ],
        ),
    ]
