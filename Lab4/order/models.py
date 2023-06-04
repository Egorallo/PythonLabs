from django.db import models
from django.urls import reverse

from cleaning.models import ServicePack
# Create your models here.

class Order(models.Model):
    # client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    client = models.CharField(max_length=100, help_text="Enter the name of the client")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    servicepack = models.ForeignKey(ServicePack, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity