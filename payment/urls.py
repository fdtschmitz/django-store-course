from django.urls import path
from . import views

urlpatterns = [

    path('payment-success', views.payment_success, name='payment-success'),  # Payment success page

    path('payment-failed', views.payment_failed, name='payment-failed'),  # Payment failed page

    path('checkout', views.checkout, name='checkout'),  # Checkout page
]