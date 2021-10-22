from rest_framework import serializers

from core.models import Can


class CanSerializer(serializers.ModelSerializer):
    """Serializer for can object"""

    class Meta:
        model = Can
        fields = ('id', 'title', 'quantity')
        read_only_fields = ('id',)
