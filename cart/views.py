from django.shortcuts import render, redirect

# Create your views here.

def cartview(request):
    ''' A view to return the contents of the shopping cart page'''
    return render(request, 'cart/cartview.html')


def add_to_cart(request, item_id):
    '''
    view to add/remove a quantiry of the specified items to cart
    '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    
    return redirect(redirect_url)

