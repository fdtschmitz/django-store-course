from django.shortcuts import render
from . models import ShippingAddress

# Create your views here.

def payment_success(request):

    return render(request, 'payment/payment-success.html')  # Payment success page

def payment_failed(request):

    return render(request, 'payment/payment-failed.html')  # Payment failed page

def checkout(request):

    #Users with account - prefill the form with their details

    if request.user.is_authenticated:

        try:

            #Authenticated users with shipping address
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = { 'shipping': shipping_address}

            return render(request, 'payment/checkout.html', context)

        except:

            #Authenticated user without shipping address

            return render(request, 'payment/checkout.html')
    

    return render(request, 'payment/checkout.html')  # Checkout page