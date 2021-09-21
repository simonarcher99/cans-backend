from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CanSerializer
from .models import Cans

class CanItemViews(APIView):
    queryset = Cans.objects.all()
    def get_object(self, pk):
        try:
            return Cans.objects.get(pk=pk)
        except Cans.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = CanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        items = Cans.objects.all()
        serializer = CanSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        can = self.get_object(pk)
        can.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


