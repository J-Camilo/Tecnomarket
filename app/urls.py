from django.urls import path, include

from .models import Marca
from .views import home, contact, galery, agregar_producto, listar_producto, error_facebook,  MarcaViewset , ProductoViewsets, MarcaSerializers, editar_producto, eliminar_producto, registro
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewsets)
router.register('marca', MarcaViewset)


#localhost:8000/api/producto
urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('galery/', galery, name='galery'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-producto/', listar_producto, name='listar_producto'),
    path('editar-producto/<id>/', editar_producto, name='editar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name='error_facebook'),
]