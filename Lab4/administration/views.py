from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin

from administration.forms import ServicePackForm
from cleaning.models import ServicePack


# Create your views here.
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def index(request):
    servicepacks = ServicePack.objects.all()
    return render(request, "administration/list_servicepack.html", {"servicepacks": servicepacks})

#
class ServicePackCreate(UserPassesTestMixin,View):
    def get(self, request):
        form = ServicePackForm()
        return render(request, 'administration/create_servicepack.html', {'form': form})

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    def post(self, request):
        form = ServicePackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:list_servicepack')
        return render(request, 'administration/create_servicepack.html', {'form': form})


# class ProductDetail(View):
#     def get(self, request, id):
#         product = get_object_or_404(Product, id=id)
#         return render(request, 'administrator/product_detail.html', {'product': product})


class ServicePackEdit(View):
    def get(self, request, id):
        servicepack = get_object_or_404(ServicePack, id=id)
        form = ServicePackForm(instance=servicepack)
        return render(request, 'administration/edit_servicepack.html', {'servicepack': servicepack, 'form': form})

    def post(self, request, id):
        servicepack = get_object_or_404(ServicePack, id=id)
        form = ServicePackForm(request.POST, instance=servicepack)
        if form.is_valid():
            form.save()
            return redirect('administration:list_servicepack')
        return render(request,'administration/edit_servicepack.html', {'servicepack': servicepack, 'form': form})


class ServicePackDelete(View):
    def get(self, request, id):
        servicepack = get_object_or_404(ServicePack, id=id)
        return render(request, 'administration/delete_servicepack.html', {'servicepack': servicepack})

    def post(self, request, id):
        servicepack = get_object_or_404(ServicePack, id=id)
        servicepack.delete()
        return redirect('administration:list_servicepack')
