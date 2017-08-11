from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=450)
    contenido = models.TextField()
    fecha = models.DateField(auto_now=False,auto_now_add=True)
    titulo_formato = models.CharField(null=True)

    def __str__(self):
        return self.titulo
