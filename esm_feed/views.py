from rest_framework import viewsets

from .serializers import UpdateSerializer
from .models import Update


def load_defaults():
    from .default import core_software
    if Update.objects.all().count() < 1:
        Update.objects.create(core_software=core_software)


load_defaults()


class ESMView(viewsets.ModelViewSet):
    """Endpoint to get the up to date Epic-Cash related versions, links, etc"""
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
