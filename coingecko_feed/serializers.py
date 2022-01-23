from rest_framework import serializers
from .models import *


class CoingeckoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coingecko
        fields = ('__all__')

    def create(self, validated_data):
        # We are overwriting one object, not saving new every time
        update, created = Coingecko.objects.update_or_create(id=1)
        Coingecko.objects.filter(id=1).update(**validated_data)
        return update


