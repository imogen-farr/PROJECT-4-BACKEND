from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.populated import PopulatedEnvironmentSerializer
from .models import Environment


class EnvironmentListView(APIView):

    def get(self, _request):
        environments = Environment.objects.all()
        serialized_environments = PopulatedEnvironmentSerializer(
            environments, many=True)
        return Response(serialized_environments.data, status=status.HTTP_200_OK)
