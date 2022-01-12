from rest_framework import serializers
from .models import *


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('__all__')

    def create(self, validated_data):
        try: update = Update.objects.filter(id=1).update(**validated_data)
        except Exception: update, created = Update.objects.get_or_create(id=1)
        update.timestamp = datetime.datetime.now()
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