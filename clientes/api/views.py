from rest_framework.viewsets import ModelViewSet
from clientes.models import Cliente, ValoresBase, Cifras, Cobros
from clientes.api.serializers import ClienteSerializer, ValoresSerializer, CifrasSerializer, CobrosSerializer

class ClientesApiViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class ValoresApiViewSet(ModelViewSet):
    serializer_class = ValoresSerializer
    queryset = ValoresBase.objects.all()

class CifrasApiViewSet(ModelViewSet):
    serializer_class = CifrasSerializer
    queryset = Cifras.objects.all()

class CobrosApiViewSet(ModelViewSet):
    serializer_class = CobrosSerializer
    queryset = Cobros.objects.all()
