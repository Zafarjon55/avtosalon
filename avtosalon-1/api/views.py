from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, CarModel, Dealer
from .serializer import CarSerializer, CarModelSerializer, DealerSerializer



class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
