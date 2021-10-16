from rest_framework import serializers
from .models import Cans

class CanSerializer(serializers.ModelSerializer):
    item = serializers.CharField(max_length=200)
    quantity = serializers.IntegerField()

    class Meta:
        model = Cans
        fields = ('__all__')