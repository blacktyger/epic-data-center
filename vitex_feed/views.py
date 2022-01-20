from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .serializers import *
from .models import *


class UpdateView(viewsets.ModelViewSet):
    """Endpoint to get the latest Vitex Exchange trading data for EPIC-002_BTC-000 pair"""
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class HistoryView(viewsets.ModelViewSet):
    """Endpoint to get historical Vitex Exchange trading data for EPIC-002_BTC-000 pair"""
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class HoldersView(viewsets.ModelViewSet):
    """Endpoint to get Vitex Holders data from ViteScan.io API"""
    serializer_class = HoldersSerializer
    queryset = Holders.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly, )

