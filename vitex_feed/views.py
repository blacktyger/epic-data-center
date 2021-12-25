from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import VitexUpdate


class VitexUpdateView(viewsets.ModelViewSet):
    """Endpoint to get VitexUpdate data"""
    serializer_class = VitexUpdateSerializer

    def get_queryset(self):
        queryset = VitexUpdate.objects.all()
        return queryset