from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente, ValoresBase, Cifras, Cobros

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nombres','apellidos','medidor','cedula','email']

class ValoresSerializer(ModelSerializer):
    class Meta:
        model = ValoresBase
        fields = ['id','valor_cifra_base','valor_adicional','base','porcentaje_mora']

class CifrasSerializer(ModelSerializer):
    class Meta:
        model = Cifras
        fields = ['id','id_usuario','mes','anio','cifra','estado']

class CobrosSerializer(ModelSerializer):
    class Meta:
        model = Cobros
        fields = ['id','id_usuario','registro','fechacifra','total']
        read_only_fields =('registro',)

