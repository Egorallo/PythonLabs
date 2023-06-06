from django.shortcuts import render, redirect
from django.views import generic
from cleaning.models import ServicePack
from .models import OrderItem
from cart.cart import Cart
from .models import Order
from django.core.exceptions import PermissionDenied
from statistics import mean, mode, median
from collections import Counter




def order_create(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("No access")

    cart = Cart(request)

    if cart.get_total_price() == 0:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        order = Order.objects.create(client=request.user.username)
        for item in cart:
            servicepackinstance = item['servicepackinstance']
            OrderItem.objects.create(
                order=order,
                servicepackinstance=servicepackinstance,
                price=item['price'],
                quantity=item['quantity']
            )
            servicepackinstance.purchase_count += item['quantity']
            servicepackinstance.status = 'o'
            servicepackinstance.save()

        cart.clear()

        return render(request, 'order/created.html', {'order': order})

    return render(request, 'order/create.html', {'cart': cart})


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
            item_list.extend([item.servicepackinstance for item in order.items.all() if item.servicepackinstance])

        # Calculate statistical measures
        sales_mean = round(mean(sales_list), 2) if sales_list else 0
        sales_mode = mode(sales_list) if sales_list else 0
        sales_median = median(sales_list) if sales_list else 0

        # Calculate the most popular item
        item_count = Counter(item_list)
        popular_item = item_count.most_common(1)[0][0].service_pack.naming if item_count else None

        # Calculate the item with the most profit
        item_profit_dict = {}
        for order in order_list:
            for item in order.items.all():
                if item.servicepackinstance:
                    profit = (item.price - item.servicepackinstance.price) * item.quantity
                    if item.servicepackinstance not in item_profit_dict:
                        item_profit_dict[item.servicepackinstance] = profit
                    else:
                        item_profit_dict[item.servicepackinstance] += profit

        item_with_most_profit = max(item_profit_dict, key=lambda item: item_profit_dict[
            item]).service_pack.naming if item_profit_dict else None

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
