from django.shortcuts import render
from . models import ShippingAddress, Order, OrderItem
from cart.cart import Cart
from django.http import JsonResponse
from decouple import config

# Create your views here.

def payment_success(request):

    #Clear the shopping cart

    for key in list(request.session.keys()):

        if key == 'session_key':
            del request.session[key]

    return render(request, 'payment/payment-success.html')  # Payment success page

def payment_failed(request):

    return render(request, 'payment/payment-failed.html')  # Payment failed page

def checkout(request):

    #Users with account - prefill the form with their details

    if request.user.is_authenticated:

        try:

            #Authenticated users with shipping address
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = { 'shipping': shipping_address,
                        'paypal_client_id': config('PAYPAL_CLIENT_ID'),
                       }

            return render(request, 'payment/checkout.html', context)

        except:

            #Authenticated user without shipping address
            context = { 'paypal_client_id': config('PAYPAL_CLIENT_ID') }
            return render(request, 'payment/checkout.html', context)
    

    return render(request, 'payment/checkout.html')  # Checkout page

def complete_order(request):

    if request.POST.get('action') == 'post':

        # Get the form data

        name = request.POST.get('name')

        email = request.POST.get('email')

        
        address1 = request.POST.get('address1')

        address2 = request.POST.get('address2')

        city = request.POST.get('city')

        state = request.POST.get('state')

        zipcode = request.POST.get('zipcode')

        if config('DEBUG'):
            print(name, email, address1, address2, city, state, zipcode)

        shipping_address = (address1 + "\n" + address2 + "\n" + city + "\n" + state + "\n" + zipcode)

        cart = Cart(request)

        total_cost = cart.get_total()

        # Create a new order for authenticated users

        if request.user.is_authenticated:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost, user=request.user)

            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'], user=request.user)
        
        # Create a new order for guest users

        else:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost)

            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'])

        order_success = True

        response = JsonResponse({'success': order_success})


    return response