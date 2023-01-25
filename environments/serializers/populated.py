from .common import EnvironmentSerializer
from pets.serializers import PetSerializer


class PopulatedEnvironmentSerializer(EnvironmentSerializer):

    pets = PetSerializer(many=True)
