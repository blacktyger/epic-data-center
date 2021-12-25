from rest_framework import serializers
from .models import *

class VitexUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitexUpdate
        fields = ('__all__')