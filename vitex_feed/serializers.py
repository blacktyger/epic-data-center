from rest_framework import serializers
from .models import *

class VitexHoldersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitexHoldersUpdate
        fields = ('__all__')