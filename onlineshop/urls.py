from django.urls import path
from onlineshop.views import OrderView

urlpatterns = [
    path('orders/', OrderView.as_view(), name='order-create'),
]