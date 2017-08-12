from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=450)
    contenido = models.TextField()
    fecha = models.DateField(auto_now=False,auto_now_add=True)
    titulo_formato = models.CharField(max_length=80,null=True)

    def __str__(self):
        return self.titulo

    def crear_titulo_formateado(self):
        self.save()
        titulo = self.titulo
        titulo = titulo.split()
        titulo_formateado = str(self.pk) +'-' + '-'.join(titulo)

        self.titulo_formato = titulo_formateado

        self.save()

    class Admin:
        list_display = ('titulo', 'fecha' , 'titulo_formato')
        list_filter = ('titulo', 'fecha')
        ordering = ('-fecha')
        search_fields = ('titulo')


class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateField(auto_now=False,auto_now_add=True)
    publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.fecha) + ' Comentario hecho a la publicacion:  ' +str(self.publicacion)


    class Admin:
        ordering = ('-fecha')
        search_fields = ('contenido')
