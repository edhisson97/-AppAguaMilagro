from django.contrib import admin
from clientes.models import Cliente, ValoresBase, Cifras, Cobros
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombres','apellidos','medidor','cedula','email']

@admin.register(ValoresBase)
class ValoresAdmin(admin.ModelAdmin):
    list_display = ['id','valor_cifra_base','valor_adicional','base','porcentaje_mora']

@admin.register(Cifras)
class CifrasAdmin(admin.ModelAdmin):
    list_display = ['id','id_usuario','mes','anio','cifra','estado']

@admin.register(Cobros)
class CobrosAdmin(admin.ModelAdmin):
    list_display = ['id','id_usuario','registro','fechacifra','total']