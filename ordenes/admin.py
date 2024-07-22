from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usuario, Maquinaria, OrdenTrabajo

admin.site.register(Usuario)
admin.site.register(Maquinaria)
admin.site.register(OrdenTrabajo)
