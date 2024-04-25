from django.shortcuts import render, redirect, reverse

# Create your views here.


def order_px(request):

    template = "prescription/order_px.html"
    # context = {
    #     'form': form
    # }

    return render(request, template)