from rest_framework import viewsets, status, permissions
from .serializers import CartSerializer
from rest_framework.response import Response

from ..models import Cart
from apps.Flat.models import Flats
from apps.Flat.api.serializers import FlatsSerializer


class CartAPIViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        user = request.user
        flats = Flats.objects.filter(cart_flats__user_id=user)
        serializer = FlatsSerializer(flats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



