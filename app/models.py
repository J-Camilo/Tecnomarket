from distutils.command.upload import upload
from email.mime import image
from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    image = models.ImageField(upload_to = "productos", null=True) 

    def __str__(self):
        return self.nombre


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to="productos")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


opctions= [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_de_consulta = models.IntegerField(choices=opctions)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
