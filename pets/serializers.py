from rest_framework import serializers
from .models import Pet
from environments.serializers.common import EnvironmentSerializer
from lifespans.serializers.common import LifespanSerializer
from jwt_auth.serializers.common import UserSerializer
from comments.serializers.populated import PopulatedCommentSerializer


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet  # the model it should use
        fields = '__all__'  # which fields to serialize


class PopulatedPetSerializer(PetSerializer):
    environments = EnvironmentSerializer()
    comments = PopulatedCommentSerializer(many=True)
    lifespans = LifespanSerializer()
    owner = UserSerializer()
