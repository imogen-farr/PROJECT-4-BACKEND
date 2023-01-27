from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Pet
from .serializers import PetSerializer, PopulatedPetSerializer


class PetListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        pets = Pet.objects.all()  # get everything from the shows table in the db
        # run everything through the serializer
        serialized_pets = PetSerializer(pets, many=True)
        # return the response and a status
        return Response(serialized_pets.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        pet_to_add = PetSerializer(data=request.data)
        try:
            pet_to_add.is_valid()
            pet_to_add.save()
            return Response(pet_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            res = {
                "detail": str(e)
            }

            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PetDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # show this one first

    def get_pet(self, pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise NotFound(detail="Can't find that pet!")

    def get(self, _request, pk):
        # we use a keywprd argument so we don't have to pass self through to get_pet
        pet = self.get_pet(pk=pk)
        serialized_pet = PopulatedPetSerializer(pet)
        return Response(serialized_pet.data, status=status.HTTP_200_OK)


def put(self, request, pk):
    pet_to_edit = self.get_pet(pk=pk)
    updated_pet = PetSerializer(pet_to_edit, data=request.data)
    try:
        updated_pet.is_valid()
        updated_pet.save()
        return Response(updated_pet.data, status=status.HTTP_202_ACCEPTED)

    except AssertionError as e:
        return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
        return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def delete(self, _request, pk):
    pet_to_delete = self.get_pet(pk=pk)
    pet_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
