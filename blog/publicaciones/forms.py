from django import forms
from .models import Comentario, Publicacion


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido','publicacion']


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo','contenido']
