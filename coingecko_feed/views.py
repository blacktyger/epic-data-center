from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .serializers import *
from .models import *


class CoingeckoView(viewsets.ModelViewSet):
    """Endpoint to get the latest Coingecko trading data for EPIC"""
    queryset = Coingecko.objects.all()
    serializer_class = CoingeckoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )