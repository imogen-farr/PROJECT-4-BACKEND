from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.populated import PopulatedLifespanSerializer
from .serializers.common import LifespanSerializer
from .models import Lifespan


class LifespanListView(APIView):

    def get(self, _request):
        lifespans = Lifespan.objects.all()
        serialized_lifespans = LifespanSerializer(
            lifespans)
        return Response(serialized_lifespans.data, status=status.HTTP_200_OK)


class LifespanDetailView(APIView):
    def get(self, _request, pk):
        lifespan = Lifespan.objects.get(pk=pk)
        serialized_lifespan = PopulatedLifespanSerializer(lifespan)
        return Response(serialized_lifespan.data, status=status.HTTP_200_OK)
