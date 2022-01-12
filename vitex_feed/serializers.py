from rest_framework import serializers
from .models import *


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('__all__')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('__all__')


class HoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holders
        fields = ('__all__')