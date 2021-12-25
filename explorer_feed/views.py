import json

from django.views.generic import CreateView, UpdateView
from django.http import JsonResponse
from rest_framework import viewsets

from .serializers import *
from .models import Block


class BlockView(viewsets.ModelViewSet):
    """Endpoint to get block/s data"""
    serializer_class = BlockSerializer

    def get_queryset(self):
        queryset = Block.objects.all()
        height = self.request.query_params.get('height')

        if height:
            queryset = queryset.filter(height=height)

        return queryset


# class UpdateBlockView(CreateView, UpdateView):
#     """
#     Use to add or update block details in EPIC blockchain
#     endpoint: 'block/<height>'
#     """
#     model = Block
#
#     def post(self, request, *args, **kwargs):
#         response = {'error': 1, 'msg': 'unknown error', 'data': None}
#         payload = json.loads(request.body)
#         print(payload)
#
#         return JsonResponse(response)