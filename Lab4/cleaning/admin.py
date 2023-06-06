from django.contrib import admin
from .models import Service, ServicePack, ServicePackInstance


class ServicePackInstanceInline(admin.TabularInline):
    model = ServicePackInstance
    extra = 0
    fields = ('id', 'price', 'date_created', 'status')


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


# Register your models here.
admin.site.register(Service)
