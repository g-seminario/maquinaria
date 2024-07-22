from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
        
class Maquinaria(models.Model):
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class OrdenTrabajo(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('verificada', 'Verificada'),
    ]
    operador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ordenes_trabajo')
    tractor = models.ForeignKey(Maquinaria, on_delete=models.CASCADE, related_name='ordenes_trabajo')
    labor = models.CharField(max_length=255)
    implemento = models.ForeignKey(Maquinaria, on_delete=models.CASCADE, related_name='implementos')
    cantidad_combustible = models.FloatField()
    horas_planificadas = models.FloatField()
    horas_reales = models.FloatField(null=True, blank=True)
    supervisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ordenes_supervisadas')
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    firma_supervisor = models.CharField(max_length=255, null=True, blank=True)