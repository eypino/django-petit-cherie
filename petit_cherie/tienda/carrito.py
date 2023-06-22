class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] ={}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self,product):
        id = str(product.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": product.id,
                "nombre": product.producto,
                "precio": product.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += product.precio
        self.save()
 
    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def decrement(self,product):
        id = str(product.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= product.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(product)
            self.save()

    def remove(self,product):
        id = str(product.id)
        if id not in self.carrito:
            del self.carrito[id]
            self.save()    
    
    def clear(self):
        self.session["carrito"] ={}
        self.session.modified = True