from django.shortcuts import render

# Create your views here.

def cartview(request):
    ''' A view to return the contents of the shopping cart page'''
    return render(request, 'cart/cartview.html')