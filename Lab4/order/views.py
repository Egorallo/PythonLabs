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


from statistics import mean, mode, median

from collections import Counter

from collections import Counter

class OrderListView(generic.ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the list of clients and products in alphabetical order
        client_list = Order.objects.order_by('client').values_list('client', flat=True).distinct()
        product_list = ServicePack.objects.order_by('naming')

        # Calculate the total sales amount and iterate through each order to get total cost and profit
        total_sales = 0
        sales_list = []
        item_list = []
        order_list = self.get_queryset()
        for order in order_list:
            total_sales += order.get_total_cost()
            sales_list.append(order.get_total_cost())
            item_list.extend([item.servicepack for item in order.items.all()])

        # Calculate statistical measures
        sales_mean = mean(sales_list) if sales_list else 0
        sales_mode = max(Counter(sales_list), key=Counter(sales_list).get) if sales_list else None
        sales_median = median(sales_list) if sales_list else 0
        popular_item = max(Counter(item_list), key=Counter(item_list).get) if item_list else None

        # Calculate the item with the most profit
        item_profit_dict = {}
        for order in order_list:
            for item in order.items.all():
                profit = (item.price - item.servicepack.price) * item.quantity
                if item.servicepack not in item_profit_dict:
                    item_profit_dict[item.servicepack] = profit
                else:
                    item_profit_dict[item.servicepack] += profit

        item_with_most_profit = max(item_profit_dict, key=item_profit_dict.get) if item_profit_dict else None

        context['client_list'] = client_list
        context['product_list'] = product_list
        context['total_sales'] = total_sales
        context['sales_mean'] = sales_mean
        context['sales_mode'] = sales_mode
        context['sales_median'] = sales_median
        context['popular_item'] = popular_item
        context['item_with_most_profit'] = item_with_most_profit

        return context





class OrderDetailView(generic.DetailView):
    model = Order
