from django.shortcuts import render
from .models import ServicePack, Order, ServicePackInstance, Service
# Create your views here.


def index(request):
    """View function for home page of site."""

    num_service_packs = ServicePack.objects.all().count()
    num_instances = ServicePackInstance.objects.all().count()
    num_instances_available = ServicePackInstance.objects.filter(status__exact='a').count()
    num_orders = Order.objects.count()

    context = {
        'num_service_packs': num_service_packs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_orders': num_orders,
    }

    return render(request, 'index.html', context=context)
