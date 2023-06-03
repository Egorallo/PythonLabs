from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import ServicePack, Order, ServicePackInstance, Service
from django.views import generic


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

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


class ServicePackListView(generic.ListView):
    model = ServicePack
    paginate_by = 2


class ServicePackDetailView(generic.DetailView):
    model = ServicePack
