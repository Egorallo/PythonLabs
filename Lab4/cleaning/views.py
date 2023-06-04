from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import ExtendedUserCreationForm
from .models import ServicePack, ServicePackInstance, Service
from django.views import generic

# Define the user roles
UNAUTHORIZED_ROLE = 'Unauthorized'
CUSTOMER_ROLE = 'Customer'
STAFF_ROLE = 'Staff'
ADMIN_ROLE = 'Admin'



# Create your views here.


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign the appropriate role based on the form data
            user_role = form.cleaned_data['user_role']
            if user_role == 'staff':
                group = Group.objects.get_or_create(name='Staff')[0]
                user.groups.add(group)
            elif user_role == 'admin':
                group = Group.objects.get_or_create(name='Admin')[0]
                user.groups.add(group)
            else:
                group = Group.objects.get_or_create(name='Customer')[0]
                user.groups.add(group)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    """View function for home page of site."""

    num_service_packs = ServicePack.objects.all().count()
    num_instances = ServicePackInstance.objects.all().count()
    num_instances_available = ServicePackInstance.objects.filter(status__exact='a').count()
    #num_orders = Order.objects.count()

    context = {
        'num_service_packs': num_service_packs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        #'num_orders': num_orders,
    }

    return render(request, 'index.html', context=context)


class ServicePackListView(generic.ListView):
    model = ServicePack
    paginate_by = 2


class ServicePackDetailView(generic.DetailView):
    model = ServicePack
