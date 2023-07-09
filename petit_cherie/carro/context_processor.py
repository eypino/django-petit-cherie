def valor_total_carro(request):
    total = 0
    carro = request.session.get("carro", {})
    for key, value in carro.items():
        precio = int(value.get("precio", 0))
        total += precio 
    return {"valor_total_carro": total}