from rest_framework import serializers
from ..models import Lifespan


class LifespanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lifespan
        fields = '__all__'
