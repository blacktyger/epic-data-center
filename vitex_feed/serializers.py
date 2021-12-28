from rest_framework import serializers
from .models import *


class VitexUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitexUpdate
        fields = ('__all__', )


class VitexHoldersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitexHoldersUpdate
        fields = ('__all__', )