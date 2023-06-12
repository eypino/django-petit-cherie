from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    tiendas=tienda.objects.all()
    context={'tiendas':tiendas}
    return render(request, 'index.html', context)

def tienda (request):
    template = loader.get_template('tienda.html')
    return HttpResponse(template.render())
