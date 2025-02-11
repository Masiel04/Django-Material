from django.db import models

# Create your models here.
class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    foto_mat=models.FileField(upload_to='material', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Distribuidor(models.Model):
    id_dist = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Almacen(models.Model):
    id_alm = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    id_pedido = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f"Pedido de {self.material.nombre} a {self.distribuidor.nombre}"
    
