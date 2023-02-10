from rest_framework import generics

from .serializers import ItemSerializer
from items.models import Item


class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
