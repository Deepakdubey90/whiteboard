# encoding=utf-8
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from models import VehicalParking
from serializer import VehicalParkingSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


def switch_to_desire_language(request):
    """
    Sholud change the language in session.
    """
    print(request)
    request.session['lang'] = 'en'


def CreateVehicalView(request, template_name='create_vehical.html'):
    """
    """
    vehicals = [{'key':'TRUCK'},
                {'key': 'SUV'},
                {'key':'CAR'},
                {'key':'BYKE'},
                {'key':'CYCLE'}]
    return render(request, template_name, {'data': vehicals})


class VehicalList(generics.ListCreateAPIView):
    """
    should create/return api list.
    """
    queryset = VehicalParking.objects.all()
    serializer_class = VehicalParkingSerializer


class VehicalDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    should retrieve/update/delete vehicals.
    """
    queryset = VehicalParking.objects.all()
    serializer_class = VehicalParkingSerializer

