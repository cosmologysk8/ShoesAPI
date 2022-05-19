from django.urls import path
from .views import start_index, crear_shoes, editar_shoes, cargar_zapatillas, borrar_shoes, detalle_zapatilla

urlpatterns = [
    path('index/', start_index),
    path('zapatillas/', cargar_zapatillas),
    path('zapatillas/crear/', crear_shoes, name='crear_shoes'),
    path('zapatillas/<int:id>', detalle_zapatilla, name='detalle_zapatilla'),
    path('zapatillas/editar/<int:id>', editar_shoes, name='editar_shoes'),
    path('zapatillas/borrar/<int:id>', borrar_shoes, name='borrar_shoes')
]