from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import *
from .models import *


class UpdateView(viewsets.ModelViewSet):
    """Endpoint to get the latest Vitex Exchange trading data for EPIC-001_BTC-000 pair"""

    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def post(self, request, *args, **kwargs):
        print(request, *args, **kwargs)


class HistoryView(viewsets.ModelViewSet):
    """Endpoint to get historical Vitex Exchange trading data for EPIC-001_BTC-000 pair"""
    serializer_class = HistorySerializer
    queryset = History.objects.all()


class HoldersView(viewsets.ModelViewSet):
    """Endpoint to get Vitex Holders data from ViteScan.io API"""
    serializer_class = HoldersSerializer
    queryset = Holders.objects.all()
