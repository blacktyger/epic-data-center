from rest_framework import serializers
from .models import *


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('__all__')

    def create(self, validated_data):
        update = Update.objects.get_or_create(id=1)
        new = Update(**validated_data)
        update = new
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