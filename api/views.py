from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CanSerializer
from .models import Cans

class CanItemViews(APIView):
    queryset = Cans.objects.all() 
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