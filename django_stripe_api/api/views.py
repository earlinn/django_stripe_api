import os

import stripe
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItemSerializer
from items.models import Item

stripe.api_key = os.getenv("STRIPE_TEST_KEY")


@api_view()
def buy(request, id):
    """The function to get a Stripe Session Id to pay for the selected Item."""
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="https://127.0.0.1:8000/success",
    )
    return Response({"sessionId": session.id, "session_url": session.url})


class ItemDetail(generics.RetrieveAPIView):
    """View class to get info on a particular item."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
