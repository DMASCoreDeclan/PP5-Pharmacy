from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PxForm, PxAdminForm, PxChangeStatusForm
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
        return redirect(reverse('account_login'))

    if request.method == 'POST':
        form = PxForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            form.save(commit=False)
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
        form = PxForm()

    template = "prescription/px_order.html"
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def px_admin(request):
    '''
    Display PX Orders for processing turn To Be Processed -> Processed by a
    member of the Team.
    '''
    if not request.user.is_staff:
        messages.error(request, 'You must be logged in as a member of our team\
            to use this service.')
        return redirect(reverse('account_login'))

    PX_STATUS = dict(Prescription.PX_STATUS)
    form = Prescription.objects.all()

    context = {
        'form': form,
        'PX_STATUS': PX_STATUS,
        }

    return render(request, 'prescription/px_admin.html', context)


@login_required
def edit_px_status(request, px_id):
    '''
    View to edit the status of the PX from Neing Pocessed to Processed'''
    if not request.user.is_staff:
        messages.error(request, 'You must be logged in as a member of our team\
            to use this service.')
        return redirect(reverse('account_login'))

    px = get_object_or_404(Prescription, pk=px_id)
    # strips the px_image formatting created in Form PxForm
    px_status_image = px.px_image
    if request.method == 'POST':
        px_form = PxChangeStatusForm(request.POST, request.FILES, instance=px)
        if px_form.is_valid():
            px_form.save()
            messages.success(request, 'Successfully updated PX status!')
            return redirect(reverse('px_admin'))
        else:
            messages.error(request, 'Failed to update the PX status. Please \
                ensure the form is valid.')
    else:
        px_form = PxChangeStatusForm(instance=px)
        # messages.info(request, f'You are editing {px_order_number}')

    template = 'prescription/edit_px_status.html'
    context = {
        'px_form': px_form,
        'px': px,
        'px_status_image': px_status_image,
    }

    return render(request, template, context)
