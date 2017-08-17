from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'publicaciones'
urlpatterns = [
    url(r'^c-p$', views.crearPublicacion, name='crearPublicacion'),
    url(r'^m-p/(?P<titulo_formateado>[a-zA-Z0-9-]+)', views.modificarPublicacion, name='modificarPublicacion'),
    url(r'^(?P<titulo_formateado>[a-zA-Z0-9-]+)', views.detalle, name='detalle'),
]
