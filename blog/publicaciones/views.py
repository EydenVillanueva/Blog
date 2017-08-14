from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publicacion

def index(request):
    return HttpResponse("Ok")

def detalle(request, titulo_formateado):
    publicacion = get_object_or_404(Publicacion, titulo_formato=titulo_formateado)
    context = { 'publicacion':publicacion}
    return render(request,'publicaciones/detalle_publicacion.html', context)
    