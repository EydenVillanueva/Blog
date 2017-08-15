from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Publicacion
from .forms import ComentarioForm

def index(request):
    return HttpResponse("Ok")

def detalle(request, titulo_formateado):
    publicacion = get_object_or_404(Publicacion, titulo_formato=titulo_formateado)
    form = ComentarioForm(request.POST or None)
    form.publicacion = publicacion
    if form.is_valid():

        form.save()
        form = ComentarioForm()

    context = { 'publicacion':publicacion,
                'form':form }
    return render(request,'publicaciones/detalle_publicacion.html', context)
