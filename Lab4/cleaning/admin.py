from django.contrib import admin
from .models import Order, Service, ServicePack, ServicePackInstance


class ServicePackInstanceInline(admin.TabularInline):
    model = ServicePackInstance
    extra = 0


class ServicePackInline(admin.TabularInline):
    model = ServicePack
    extra = 0


@admin.register(ServicePack)
class ServicePackAdmin(admin.ModelAdmin):
    list_display = ('naming', 'display_service')
    inlines = [ServicePackInstanceInline]


@admin.register(ServicePackInstance)
class ServicePackInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_pack', 'price', 'date_created')
    list_filter = ('status', 'date_created')

    fieldsets = (
        (None, {
            'fields': ('service_pack', 'price', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'date_created')
        }),
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'address', 'date_of_completion')
    fields = ['code', ('address', 'date_of_completion')]
    #inlines = [ServicePackInstanceInline]


# Register your models here.
admin.site.register(Service)
# admin.site.register(ServicePack)
# admin.site.register(ServicePackInstance)
admin.site.register(Order, OrderAdmin)
