class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro")
        if not self.carro:
            self.carro = self.session["carro"] = {}
        else:
            self.carro=self.carro

    def agregar(self, producto):
        if str(producto.id_producto) not in self.carro.keys():
            self.carro[str(producto.id_producto)] = {
                "producto_id": producto.id_producto,
                "nombre": producto.nombre_producto,
                "precio": str(producto.valor_prod),
                "cantidad": 1,
                "imagen": producto.imagen_prod.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id_producto):
                    value["cantidad"] += 1
                    value["precio"]=int(value["precio"])+producto.valor_prod
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()


    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id_producto):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=int(value["precio"])-producto.valor_prod
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True