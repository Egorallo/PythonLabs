from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cleaning.models import ServicePack
from .cart import Cart
from .forms import CartAddServicePackForm
from django.core.exceptions import PermissionDenied

@require_POST
def cart_add(request, servicepack_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("Net dostupa")

    cart = Cart(request)
    servicepack = get_object_or_404(ServicePack, id=servicepack_id)
    form = CartAddServicePackForm(request.POST)
    # if form.is_valid():
    #cd = form.cleaned_data
    # cart.add(servicepack=servicepack,
    #          quantity=cd['quantity'],
    #          update_quantity=cd['update'])
    cart.add(servicepack=servicepack, quantity=1)
    return redirect('cart:cart_detail')

def cart_remove(request, servicepack_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("Net dostupa")

    cart = Cart(request)
    servicepack = get_object_or_404(ServicePack, id=servicepack_id)
    cart.remove(servicepack)
    return redirect('cart:cart_detail')

def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Net dostupa")
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})