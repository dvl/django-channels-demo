from rest_framework import serializers

from . import models


class LanceSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()

    class Meta:
        model = models.Lance
        fields = '__all__'
