 # -*- encoding: utf-8 -*-
from django.db import models


TYPE_CHOICES = (
    ('truck','TRUCK'),
    ('suv', 'SUV'),
    ('car','CAR'),
    ('byke','BYKE'),
    ('cycle','CYCLE'),
)


class VehicalParking(models.Model):
    """
    Should create vehical parking info.
    """

    vehical_name = models.CharField(max_length=30)
    vehical_number = models.CharField(max_length=50)
    vehical_type = models.CharField(
        max_length=30, choices=TYPE_CHOICES, default='cycle'
    )
    vehical_intime = models.TimeField(blank=False, null=False)
    vehical_outtime = models.TimeField(blank=False, null=False)
    park_fare = models.CharField(max_length=100)


    def __str__(self):
        return unicode(self.vehical_name)
