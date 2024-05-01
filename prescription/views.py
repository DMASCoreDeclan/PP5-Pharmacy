from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PrescriptionForm
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
            form.instance.user = request.user
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

    template = "prescription/order_px.html"
    context = {
        'form': form
    }

    return render(request, template, context)