from django.db import models
from django.contrib.auth.models import User

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
    status = [
        ('0', 'To be Processed'),
        ('1', 'Being Processed'),
        ('2', 'Processed'),
        ('3', 'Cannot be Processed'),
    ]

    delivery = [
        ('0', 'Being Collected'),
        ('1', 'Being Delivered'),
    ]
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='prescription_user'
        )  
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    date_required = models.DateTimeField(auto_now=True)
    dr_full_name = models.CharField(max_length=50, null=False, blank=False)
    px_image = models.ImageField(null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    px_status = models.CharField(max_length=20, choices=status, default=0)
    px_delivery = models.CharField(max_length=50, choices=delivery, default=0)