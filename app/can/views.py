from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


from core.models import Can

from can.serializers import CanSerializer


class CanViewSet(viewsets.ModelViewSet):
    """Base viewset for user owned recipe attributes"""
    serializer_class = CanSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Can.objects.all()

    def perform_create(self, serializer):
        """Create a new object"""
        # Need to change so that only currently authenticated users cans are checked
        title = serializer.validated_data['title']
        if len(self.queryset.filter(title=title)) > 0:
            return JsonResponse({'status': 400, 'content': 'Can already exists'})
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
