from django.shortcuts import render
from django.views import generic

from .models import OrderItem
from cart.cart import Cart
# from cleaning.models import Client
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("net dostpa")

    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=request.user.username)

        for item in cart:
            OrderItem.objects.create(order=order,
                                     servicepack=item['servicepack'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            item['servicepack'].purchase_count += item['quantity']
            item['servicepack'].save()

        cart.clear()
        return render(request, 'order/created.html',
                      {'order': order})

    return render(request, 'order/create.html',
                  {'cart': cart})


class OrderListView(generic.ListView):
    model = Order


class OrderDetailView(generic.DetailView):
    model = Order
