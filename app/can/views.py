from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
        serializer.save(user=self.request.user)
