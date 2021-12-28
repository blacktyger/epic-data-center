from rest_framework import viewsets

from .serializers import *
from .models import *


class VitexUpdateView(viewsets.ModelViewSet):
    """Endpoint to get VitexUpdate data"""
    serializer_class = VitexUpdateSerializer

    def get_queryset(self):
        queryset = VitexUpdate.objects.all()
        return queryset


class VitexHoldersUpdateView(viewsets.ModelViewSet):
    """Endpoint to get VitexHoldersUpdate data"""
    serializer_class = VitexHoldersUpdateSerializer

    def get_queryset(self):
        queryset = VitexHoldersUpdate.objects.all()
        return queryset