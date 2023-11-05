from django.contrib import admin
from usuarios.models import Usuarios, Compra

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    ...

class CompraAdmin(admin.ModelAdmin):
    ...

admin.site.register(Usuarios,UsuarioAdmin)

admin.site.register(Compra,CompraAdmin)
