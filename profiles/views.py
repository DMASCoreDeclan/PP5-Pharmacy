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


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for {order_number}.  '
        'A confirmation email was sent on that date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def px_order_history(request, px_order_number):
    px_order = get_object_or_404(Prescription, px_order_number=px_order_number)

    print(px_order_number)

    messages.info(request, (
        f'This is a past confirmation for {px_order_number}.  '
        'A confirmation email was sent on that date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'px_order': px_order,
        'from_profile': True,
    }

    return render(request, template, context)