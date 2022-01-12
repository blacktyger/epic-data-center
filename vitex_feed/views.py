from rest_framework import viewsets
from .serializers import *
from .models import *


class VitexUpdateView(viewsets.ViewSet):
    """Endpoint to get Vitex Exchange trading data for EPIC-001_BTC-000 pair"""
    serializer_class = VitexUpdateSerializer

    def create(self, request):
        post_data = request.data
        print(post_data)

        update, created = VitexUpdate.objects.get_or_create(id=1)
        print(update, created)

    def get_queryset(self):
        queryset = VitexUpdate.objects.all()
        return queryset


class VitexHoldersUpdateView(viewsets.ModelViewSet):
    """Endpoint to get Vitex Holders data from ViteScan.io API"""
    serializer_class = VitexHoldersUpdateSerializer

    def get_queryset(self):
        queryset = VitexHoldersUpdate.objects.all()
        return queryset