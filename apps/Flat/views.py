from django.shortcuts import render
from rest_framework import generics
from .models import Flats
from .serializers import PropertySerializer



class PropertyList(generics.ListCreateAPIView):
    queryset = Flats.objects.all()
    serializer_class = PropertySerializer


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flats.objects.all()
    serializer_class = PropertySerializer