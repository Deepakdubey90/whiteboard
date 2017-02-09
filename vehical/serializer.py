 # -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import VehicalParking


class VehicalParkingSerializer(serializers.ModelSerializer):
    """
    Vehical parking seruializer.
    """
    class Meta:
        model = VehicalParking
        fields = ('id', 'vehical_name', 'vehical_number', 'vehical_type',
                  'vehical_intime', 'vehical_outtime', 'park_fare'
        )
