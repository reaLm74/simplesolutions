import os

import stripe
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from .models import Item, Order, Discount


class BuySessionView(View):
    def post(self, request, *args, **kwargs):
        you_domain = os.getenv('YOUR_DOMAIN')
        item = Item.objects.get(id=self.kwargs["item_id"])
        checkout_session = stripe.checkout.Session.create(
            line_items=[{'price_data': {
                'currency': item.currency,
                'unit_amount': item.price,
                'product_data': {'name': item.name},
            },
                'quantity': 1,
            }],
            mode='payment',
            success_url=you_domain + '/success/',
            cancel_url=you_domain + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id,
            'amount_total': checkout_session.amount_total,
            'currency': checkout_session.currency
        })


class BuyAllSessionView(View):
    def post(self, request, *args, **kwargs):
        you_domain = os.getenv('YOUR_DOMAIN')
        item = Order.objects.select_related('item').all()
        line = []
        rebate = Discount.objects.all()
        if rebate.exists():
            discount = rebate[0].discount
        else:
            discount = []
        for date in item:
            line.append(
                {'price_data': {
                    'currency': date.item.currency,
                    'unit_amount': date.item.price,
                    'product_data': {'name': date.item.name},
                },
                    'quantity': 1,

                }
            )
        checkout_session = stripe.checkout.Session.create(
            line_items=line,
            mode='payment',
            success_url=you_domain + '/success/',
            cancel_url=you_domain + '/cancel/',
            discounts=[{"coupon": discount}],
        )
        return JsonResponse({
            'id': checkout_session.id,
            'amount_subtotal': checkout_session.amount_subtotal,
            'amount_total': checkout_session.amount_total,
            'amount_discount': checkout_session.total_details.amount_discount,
        })


class AddDiscountsSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            discount = Discount.objects.all().exists()
            if not discount:
                Discount.objects.create(discount=self.kwargs["discount_id"])
                return redirect('items:order')
            else:
                return redirect('items:cancel')
        except Exception:
            return redirect('items:cancel')


class DeleteDiscountsSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            discount = Discount.objects.all()
            discount.delete()
            return redirect('items:order')
        except Exception:
            return redirect('items:cancel')


class AddOrderSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            order = Order.objects.filter(
                item_id=self.kwargs["item_id"]
            ).exists()
            if not order:
                Order.objects.create(item_id=self.kwargs["item_id"])
                return redirect('items:item', item_id=self.kwargs["item_id"])
        except Exception:
            return redirect('items:cancel')


class DeleteOrderSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            order = get_object_or_404(Order, item_id=self.kwargs["item_id"])
            order.delete()
            return redirect('items:item', item_id=self.kwargs["item_id"])
        except Exception:
            return redirect('items:cancel')
