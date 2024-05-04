from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PrescriptionForm
from profiles.models import UserProfile
from .models import Prescription 
# Create your views here.


@login_required
def order_px(request):
    '''
    View to allow users to send a picture of their PX from their Dr to the 
    Pharmacy for fulfillment.  The form will have the customers deetails,
    their Drs Name, the date sent, the date required and whether it will be
    Delivered or Collected.  It should indicate to the customer the earliest 
    time their PX might be available. 
    '''
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to use this service, \
            please login')
        return redirect(reverse('login'))

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.user_profile = request.user
            form.save()
            messages.success(
                request, 
                f'Your Prescription has been successfully sent!'
                )
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 
                f'Unfortunately something went wrong \
                    Your Prescription has not been sent!\
                        Please try again.')
    else:
        form = PrescriptionForm()

    template = "prescription/px_order.html"
    context = {
        'form': form
    }

    return render(request, template, context)


def px_admin(request):
    '''
    Display PX Orders for processing turn To Be Processed -> Processed
    '''
    PX_STATUS = dict(Prescription.PX_STATUS)
    form = Prescription.objects.all()
  
    if request.method == 'GET':
        Prescription.objects.all()
    
    if request.method == 'POST':
        form = Prescription(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                f'Your Prescription has been successfully sent!'
                )
            return redirect(reverse('px_admin'))
  
    context = {
        'form': form, 
        'PX_STATUS': PX_STATUS, 
        }

    return render(request, 'prescription/px_admin.html', context)


