from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.common import EnvironmentSerializer
from .serializers.populated import PopulatedEnvironmentSerializer
from .models import Environment


class EnvironmentListView(APIView):

    def get(self, _request):
        environments = Environment.objects.all()
        serialized_environments = EnvironmentSerializer(
            environments)
        return Response(serialized_environments.data, status=status.HTTP_200_OK)

class EnvironmentDetailView(APIView):
    def get(self, _request, pk):
      environment = Environment.objects.get(pk=pk)
      serialized_environments = PopulatedEnvironmentSerializer(environment)
      return Response(serialized_environment.data, status=status.HTTP_200_OK)