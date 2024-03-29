from rest_framework import serializers
from ..models import Flats


class FlatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flats
        fields = '__all__'

