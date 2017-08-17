from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Publicacion
from .forms import ComentarioForm, PublicacionForm


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


def crearPublicacion(request):

    form = PublicacionForm(request.POST or None)
    flag = 'nuevo'

    if form.is_valid():
        publicacion = form.save()
        publicacion.crear_titulo_formateado()
        form = PublicacionForm()

    context = {'form': form,
                'flag': flag}

    return render(request,'publicaciones/form_publicacion.html',context)


def modificarPublicacion(request, titulo_formateado):

    publicacion = get_object_or_404(Publicacion, titulo_formato=titulo_formateado)
    form = PublicacionForm(request.POST or None, instance=publicacion)
    flag = 'modificar'

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('publicaciones:detalle',publicacion.titulo_formato)

    context = {'form': form,
                'flag': flag}

    return render(request,'publicaciones/form_publicacion.html',context)
