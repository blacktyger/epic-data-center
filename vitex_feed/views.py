from rest_framework import viewsets

from .serializers import *
from .models import *


class UpdateView(viewsets.ModelViewSet):
    """Endpoint to get the latest Vitex Exchange trading data for EPIC-001_BTC-000 pair"""
    serializer_class = UpdateSerializer
    queryset = Update.objects.all()


class HistoryView(viewsets.ModelViewSet):
    """Endpoint to get historical Vitex Exchange trading data for EPIC-001_BTC-000 pair"""
    serializer_class = HistorySerializer
    queryset = HistoryUpdate.objects.all()


class HoldersView(viewsets.ModelViewSet):
    """Endpoint to get Vitex Holders data from ViteScan.io API"""
    serializer_class = HoldersSerializer
    queryset = Holders.objects.all()
