from decimal import Decimal
from django.conf import settings
from cleaning.models import ServicePack, ServicePackInstance


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, servicepackinstance, quantity=1, update_quantity=False):
        servicepackinstance_id = str(servicepackinstance.id)
        if servicepackinstance_id not in self.cart:
            self.cart[servicepackinstance_id] = {'quantity': 0,
                                                 'price': str(servicepackinstance.price)}
        if update_quantity:
            self.cart[servicepackinstance_id]['quantity'] = quantity
        else:
            self.cart[servicepackinstance_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, servicepack):
        servicepack_id = str(servicepack.id)
        if servicepack_id in self.cart:
            del self.cart[servicepack_id]
            self.save()

    def __iter__(self):
        servicepackinstance_ids = self.cart.keys()
        servicepackinstances = ServicePackInstance.objects.filter(id__in=servicepackinstance_ids)
        for servicepackinstance in servicepackinstances:
            self.cart[str(servicepackinstance.id)]['servicepackinstance'] = servicepackinstance

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
