import uuid

from django.db import models
from django.contrib.auth.models import User

from profiles.models import UserProfile

# Create your models here.

class Prescription(models.Model):
    '''
    This MODEL is for uploading a prescription(px) to be sent to the pharmacy.
    Tis model takes information from User and adds some fields to it.
    The FORM for this model will require the User to be logged in.  It will 
    take info from the UserProfile and prepopulate the form with all the 
    required information except the image of the PX and the Drs Name.  The
    PX will be delivered or Collected and payment will be COD ie - this will
    not be payable through the cart.  Within the pharamacy, they will want a 
    report on the status of online PXs, the default is set to 'To be Processed'
    The default for Collected/Delivered is 'Collected'
    '''
    PX_STATUS = [
        ('0', 'To be Processed'),
        ('1', 'Being Processed'),
        ('2', 'Processed'),
        ('3', 'Cannot be Processed'),
    ]

    PX_DELIVERY = [
        ('0', 'Being Collected'),
        ('1', 'Being Delivered'),
    ]
    
    px_order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='prescription_user'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    date_required = models.DateTimeField(auto_now=True)
    dr_full_name = models.CharField(max_length=50, null=False, blank=False)
    px_image = models.ImageField(null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    px_status = models.CharField(max_length=20, choices=PX_STATUS, default=0)
    px_delivery = models.CharField(max_length=50, choices=PX_DELIVERY, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.px_order_number:
            self.px_order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.px_order_number
