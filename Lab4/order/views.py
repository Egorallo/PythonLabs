from django.db.models import Sum
from django.shortcuts import render
from django.views import generic

from cleaning.models import ServicePack
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
    template_name = 'order/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the list of clients and products in alphabetical order
        client_list = Order.objects.order_by('client').values_list('client', flat=True).distinct()
        product_list = ServicePack.objects.order_by('naming')

        # Calculate the total sales amount and iterate through each order to get total cost
        total_sales = 0
        order_list = self.get_queryset()
        for order in order_list:
            total_sales += order.get_total_cost()

        context['client_list'] = client_list
        context['product_list'] = product_list
        context['total_sales'] = total_sales

        return context


class OrderDetailView(generic.DetailView):
    model = Order
