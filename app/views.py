from email.mime import message
from pyexpat.errors import messages
from sre_constants import SUCCESS
from tokenize import Pointfloat
from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto
from .forms import ContactoForms, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializers, MarcaSerializers

# Create your views here.

class MarcaViewset (viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializers

class ProductoViewsets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        return productos
 

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)


def contact(request):
    data = {
        'form': ContactoForms()
    }

    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Gracias por contar con nosotros"
        else:
            data['form'] = formulario

    return render(request, 'app/contact.html', data)



def galery(request):
    return render(request, 'app/galery.html')


@permission_required('app.add_producto')
def agregar_producto(request):
 
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data['form'] = formulario

    return render(request, 'app/producto/agregar.html', data)


@permission_required('app.view_producto')
def listar_producto(request):
    
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
      }
    
    return render(request, 'app/producto/listar.html', data)


@permission_required('app.change_producto')
def editar_producto(request, id):
 
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form' :  ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_producto")
        else:
            data['form'] = formulario

    return render(request, 'app/producto/modificar.html', data)


@permission_required('app.delete_producto')
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_producto")


def error_facebook (request):
    return render(request, 'registration/error_facebook.html')



def registro (request):
    data = {
        'form' :  CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="home")
        else:
            data['form'] = formulario

    return render(request, 'registration/registro.html', data)