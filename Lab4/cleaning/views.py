import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404

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
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            response = requests.get(f'https://api.agify.io/?name={name}')
            if response.status_code == 200:
                data = response.json()
                age = data.get('age')
            else:
                age = "Failed to retrieve age."
        else:
            age = None
    else:
        name = None
        age = None

    num_service_packs = ServicePack.objects.all().count()
    num_instances = ServicePackInstance.objects.all().count()
    num_instances_available = ServicePackInstance.objects.filter(status__exact='a').count()

    try:
        response = requests.get('https://api.kanye.rest/')

        if response.status_code == 200:
            data = response.json()
            quote = data["quote"]
        else:
            quote = "Failed to retrieve quote."
    except:
        quote = ""

    context = {
        'num_service_packs': num_service_packs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'quote': quote,
        'age': age,
        'name': name,
    }

    return render(request, 'index.html', context=context)


class ServicePackListView(generic.ListView):
    model = ServicePack
    template_name = 'cleaning/servicepack_list.html'  # Update with your template path

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     price_filter = self.request.GET.get('price')
    #
    #     if price_filter:
    #         queryset = queryset.filter(price__lt=price_filter)
    #
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['price_filter'] = self.request.GET.get('price')
    #     return context



class ServicePackDetailView(generic.DetailView):
    model = ServicePack
    template_name = 'cleaning/servicepack_detail.html'  # Update with your template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        servicepack = self.get_object()
        price_filter = self.request.GET.get('price')

        if price_filter:
            filtered_copies = servicepack.servicepackinstance_set.filter(price__lt=price_filter)
        else:
            filtered_copies = servicepack.servicepackinstance_set.all()

        context['filtered_copies'] = filtered_copies
        context['price_filter'] = price_filter
        return context