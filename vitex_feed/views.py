from rest_framework import viewsets

from .serializers import *
from .models import *

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


class UpdateView(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """Endpoint to get the latest Vitex Exchange trading data for EPIC-001_BTC-000 pair"""

    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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
