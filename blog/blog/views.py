from django.shortcuts import render
from publicaciones.models import Publicacion
from .forms import ContactoForm
from django.core.mail import send_mail

# Create your views here.
def inicio(request):

    lista_publicaciones = Publicacion.objects.all().order_by('fecha')

    contexto = {
        'lista_publicaciones': lista_publicaciones
    }

    return render(request,'inicio.html',contexto)


def about(request):

    contexto = {}

    return render(request, 'about.html', contexto)




def contacto(request):

    form = ContactoForm(request.POST or None)



    if form.is_valid():

        form_asunto = form.cleaned_data.get('asunto')
        form_email = form.cleaned_data.get('email')
        form_mensaje = form.cleaned_data.get('mensaje')
        form_nombre = form.cleaned_data.get('nombre')


        email_asunto = 'Form de contacto'
        email_from = form_email
        email_to = ['pedroesparzaaa@gmail.com']
        email_mensaje = '%s: %s enviado por %s' %(form_nombre, form_mensaje, form_email)

        send_mail(
            email_asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False,
        )


    contexto = {
            'form' : form
    }

    return render(request, 'contacto.html', contexto)
