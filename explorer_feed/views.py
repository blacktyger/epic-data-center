from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .serializers import *
from .models import Block


class BlockView(viewsets.ModelViewSet):
    """Endpoint to get Epic-Cash blockchain blocks data"""
    serializer_class = BlockSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = Block.objects.all()
        height = self.request.query_params.get('height')

        if height:
            queryset = queryset.filter(height=height)

        return queryset
