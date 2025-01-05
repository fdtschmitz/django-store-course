from django.db import models

from django.contrib.auth.models import User

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
