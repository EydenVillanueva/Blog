from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'publicaciones'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<titulo_formateado>[a-zA-Z0-9-]+)$', views.detalle, name='detalle'),
    #url(r'^\d+[-a-zA-Z0-9]+/$', views.detalle, name='detalle')
]
