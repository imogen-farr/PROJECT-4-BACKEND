from .common import LifespanSerializer
from pets.serializers import PetSerializer


class PopulatedLifespanSerializer(LifespanSerializer):

    pets = PetSerializer(many=True)
