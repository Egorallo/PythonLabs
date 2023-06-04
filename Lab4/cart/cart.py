from decimal import Decimal
from django.conf import settings
from cleaning.models import ServicePack


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, servicepack, quantity=1, update_quantity=False):
        servicepack_id = str(servicepack.id)
        if servicepack_id not in self.cart:
            self.cart[servicepack_id] = {'quantity': 0,
                                  'price': str(servicepack.price)}
        if update_quantity:
            self.cart[servicepack_id]['quantity'] = quantity
        else:
            self.cart[servicepack_id]['quantity'] += quantity
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
        servicepack_ids = self.cart.keys()
        servicepacks = ServicePack.objects.filter(id__in=servicepack_ids)
        for servicepack in servicepacks:
            self.cart[str(servicepack.id)]['servicepack'] = servicepack

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