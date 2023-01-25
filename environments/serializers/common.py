from rest_framework import serializers
from ..models import Environment


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        # fields = ('id', 'title') # <- can specify specific fields with a tuple
        fields = '__all__'
