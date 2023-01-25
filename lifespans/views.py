from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.populated import PopulatedLifespanSerializer
from .models import Lifespan


class LifespanListView(APIView):

    def get(self, _request):
        lifespans = Lifespan.objects.all()
        serialized_lifespans = PopulatedLifespanSerializer(
            lifespans, many=True)
        return Response(serialized_lifespans.data, status=status.HTTP_200_OK)
