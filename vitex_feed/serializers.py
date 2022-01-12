import datetime

from rest_framework import serializers
from django.utils import timezone

from .models import *


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('__all__')

    def create(self, validated_data):
        update, created = Update.objects.update_or_create(id=1)
        Update.objects.filter(id=1).update(**validated_data)
        update.timestamp = str(timezone.now())
        update.save()

        return update

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('__all__')


class HoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holders
        fields = ('__all__')