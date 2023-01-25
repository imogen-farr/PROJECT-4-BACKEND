from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet  # the model it should use
        fields = '__all__'  # which fields to serialize
        