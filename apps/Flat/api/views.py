from rest_framework.viewsets import ModelViewSet
from ..models import Flats
from .serializers import FlatsSerializer
from rest_framework import permissions


class FlatsAPIViewSet(ModelViewSet):
    queryset = Flats.objects.all()
    serializer_class = FlatsSerializer
    permission_classes = (permissions.IsAuthenticated, )

