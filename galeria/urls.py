from django.urls import path

from galeria.views import buscar, imagem, index

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]
