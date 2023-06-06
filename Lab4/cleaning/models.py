from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Service(models.Model):
    """Model for Service itself."""
    name = models.CharField(max_length=100, help_text="Enter the service to perform")

    def __str__(self):
        return self.name


class ServicePack(models.Model):
    """Model for Service Pack."""
    naming = models.CharField(max_length=200, help_text="Enter the service pack naming")
    service = models.ManyToManyField(Service, help_text='Select a service for this service pack')
    purchase_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.naming

    def get_absolute_url(self):
        return reverse('servicepack-detail', args=[str(self.id)])

    def display_service(self):
        return ', '.join(service.name for service in self.service.all()[:3])

    display_service.short_description = 'Service'


class ServicePackInstance(models.Model):
    """Specific Service pack which can or cannot be purchased."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for particular Service Pack")
    service_pack = models.ForeignKey('ServicePack', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    date_created = models.DateField(null=True, blank=True)
    purchase_count = models.PositiveIntegerField(default=0)

    AVAILABLE_STATUS = (
        ('a', 'Available'),
        ('o', 'Out of stock'),
        ('c', 'Coming soon')
    )

    status = models.CharField(
        max_length=1,
        choices=AVAILABLE_STATUS,
        blank=True,
        default='a',
        help_text='Service pack availability'
    )

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f'{self.id} '
