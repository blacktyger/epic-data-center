from rest_framework import viewsets

from .paginations import VitexPagination
from .serializers import *
from .models import *


class VitexUpdateView(viewsets.ModelViewSet):
    """Endpoint to get Vitex Exchange trading data for EPIC-001_BTC-000 pair"""
    serializer_class = VitexUpdateSerializer
    pagination_class = VitexPagination

    def get_queryset(self):
        queryset = VitexUpdate.objects.all()
        return queryset


class VitexHoldersUpdateView(viewsets.ModelViewSet):
    """Endpoint to get Vitex Holders data from ViteScan.io API"""
    serializer_class = VitexHoldersUpdateSerializer

    def get_queryset(self):
        queryset = VitexHoldersUpdate.objects.all()
        return queryset