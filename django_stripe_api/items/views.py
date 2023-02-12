import os

import stripe
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Item
from django_stripe_api.settings import MODE

stripe.api_key = f"{os.getenv('STRIPE_SECRET_KEY')}"


def buy(request, id):
    """Gets a Stripe Session Id to pay for the selected item."""
    item = get_object_or_404(Item, pk=id)
    if MODE == "dev":
        domain = get_current_site(request)
    else:
        domain = "localhost"
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
        success_url=f"http://{domain}/success",
        cancel_url=f"http://{domain}/cancel",
    )
    return JsonResponse({"id": session.id})


def item(request, id):
    """Shows info on a particular item and a buy button."""
    item = get_object_or_404(Item, pk=id)
    """ customer = stripe.Customer.create(description="My First Test Customer")
    intent = stripe.PaymentIntent.create(
        amount=item.price,
        currency="usd",
        automatic_payment_methods={"enabled": True},
        customer=customer["id"],
        metadata={
            "item_id": item.pk,
            "item_name": item.name,
            "item_description": item.description,
        },
    ) """
    context = {
        "item": item,
        "public_key": os.getenv("STRIPE_PUBLIC_KEY"),
        # "client_secret": intent["client_secret"],
    }
    return render(request, "item.html", context)


def success(request):
    """Shows a success page."""
    return render(request, "success.html")


def cancel(request):
    """Shows a cancel page."""
    return render(request, "cancel.html")


# add custom errors pages
