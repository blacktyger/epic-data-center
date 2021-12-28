from rest_framework import viewsets

from .serializers import *
from .models import *


class VitexHoldersUpdateView(viewsets.ModelViewSet):
    """Endpoint to get VitexHoldersUpdate data"""
    serializer_class = VitexHoldersUpdateSerializer

    def get_queryset(self):
        queryset = VitexHoldersUpdate.objects.all()
        return queryset