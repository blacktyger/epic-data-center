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
    # pagination_class = HistoryPagination
    # permission_classes = (IsAuthenticatedOrReadOnly, )