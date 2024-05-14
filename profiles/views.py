from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order
from prescription.models import Prescription
from .forms import UserProfileForm


@login_required
def profiles(request):
    """
    Display the Users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update your profile.  \
                Please check the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    px_orders = Prescription.objects.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'px_orders': px_orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def px_order_history(request, px_order_number):
    px_order = get_object_or_404(Prescription, px_order_number=px_order_number)

    messages.info(request, (
        f'This is a past confirmation for {px_order_number}.'
    ))

    template = 'prescription/prescription_history.html'
    context = {
        'px_order': px_order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def prescription_history(request, px_order_number):
    """
    displays the PX submitted
    """
    px_order = get_object_or_404(Prescription, px_order_number=px_order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        prescription.user = profile

        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}.')

    template = 'prescription/prescription_history.html'
    context = {
        'px_order': px_order,
    }

    return render(request, template, context)
