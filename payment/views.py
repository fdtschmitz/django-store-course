from django.shortcuts import render

# Create your views here.

def payment_success(request):

    return render(request, 'payment/payment-success.html')  # Payment success page

def payment_failed(request):

    return render(request, 'payment/payment-failed.html')  # Payment failed page

