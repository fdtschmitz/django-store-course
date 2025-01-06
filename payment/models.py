from django.db import models

from django.contrib.auth.models import User

from store.models import Product

class ShippingAddress(models.Model):

    # Shipping address model
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # Foreign key to User model - autehnticated users and not authenticated users
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  

    class Meta:
        verbose_name_plural = 'Shipping Addresses'
    

    def __str__(self):
        return 'Shipping address - ' + str(self.id)


class Order(models.Model):

    # Order model
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    shipping_address = models.TextField(max_length=10000)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    #FK to User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Order - #' + str(self.id)


class OrderItem(models.Model):
    #FK
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    # Order item model
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # FK to Order model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Order item - #' + str(self.id)
    