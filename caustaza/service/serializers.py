from .models import Services
from rest_framework import serializers

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(read_only=True, many=True)
    class Meta:
        model = Services
        fields = '__all__'