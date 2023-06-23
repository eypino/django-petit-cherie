from decimal import Decimal
from django.conf import settings
from tienda.models import Producto
class cart(object):

    def__init__(self,request):
    #initializing cart
        self.session=request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.sessions[sessions.CART_SESSION_ID]={}
        self.cart=cart

    def add(self,product,quantity=1,override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0, 'price':str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity'] += quantity       
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()        

    def __iter__(self):
        producto_ids = self.cart.keys()
        product = Producto.objects.filter(id__in=producto_ids)

        cart = self.cart.copy()
        for product in productos:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price'] * item['quantity']
            yield item    