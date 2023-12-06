from django.urls import path

from items.service import (
    BuySessionView,
    AddOrderSessionView,
    DeleteOrderSessionView,
    BuyAllSessionView,
    AddDiscountsSessionView,
    DeleteDiscountsSessionView,
)
from items.views import (
    ItemPageView,
    SuccessView,
    CancelView,
    ItemIndex,
    OrderIndex,
)

app_name = 'items'

urlpatterns = [
    path('item/<item_id>/', ItemPageView.as_view(), name='item'),
    path('buy/<item_id>/', BuySessionView.as_view(), name='buy'),
    path('buy_all/', BuyAllSessionView.as_view(), name='buy_all'),
    path('add/<item_id>/', AddOrderSessionView.as_view(), name='add'),
    path('delete/<item_id>/', DeleteOrderSessionView.as_view(), name='delete'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('index/', ItemIndex.as_view(), name='index'),
    path('order/', OrderIndex.as_view(), name='order'),
    path('discount/<discount_id>/', AddDiscountsSessionView.as_view(),
         name='discount'),
    path('delete_discount/', DeleteDiscountsSessionView.as_view(),
         name='delete_discount'),
]
