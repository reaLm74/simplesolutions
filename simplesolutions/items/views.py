import os

import stripe
from django.views.generic import ListView
from django.views.generic import TemplateView
from dotenv import load_dotenv

from .models import Item, Order, Discount

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class ItemIndex(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'


class ItemPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, item_id, **kwargs):
        stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
        item = Item.objects.get(id=item_id)
        button = True
        if Order.objects.filter(item_id=item_id).exists():
            button = False
        context = super().get_context_data(**kwargs)
        context.update({
            "button": button,
            "item": item,
            "STRIPE_PUBLIC_KEY": stripe_public_key
        })
        return context


class OrderIndex(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'orders'

    def get_queryset(self, *args, **kwargs):
        return Order.objects.select_related('item').all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        button = True
        button_pay = False
        if Discount.objects.all().exists():
            button = False
        if self.object_list.exists():
            button_pay = True
        context['button'] = button
        context['button_pay'] = button_pay
        return context


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
