from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido','publicacion']


class CrearPublicacionForm(forms.ModelForm):
    class meta:
        model = Publicacion
        fields = ['titulo','contenido']

        labels = {
            'titulo':_('Título de la Publicación: ')
            'contenido':_('Contenido de la Publicación: ')
        }

        widgets = {
            'contenido': Textarea(attrs={'col': 80, 'rows': 20})
        }
