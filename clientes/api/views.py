from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from clientes.models import Cliente, ValoresBase, Cifras, Cobros
from clientes.api.serializers import ClienteSerializer, ValoresSerializer, CifrasSerializer, CobrosSerializer

class ClientesApiViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]

class ValoresApiViewSet(ModelViewSet):
    serializer_class = ValoresSerializer
    queryset = ValoresBase.objects.all()
    permission_classes = [permissions.AllowAny]

class CifrasApiViewSet(ModelViewSet):
    serializer_class = CifrasSerializer
    queryset = Cifras.objects.all()
    permission_classes = [permissions.AllowAny]

class CobrosApiViewSet(ModelViewSet):
    serializer_class = CobrosSerializer
    queryset = Cobros.objects.all()
    permission_classes = [permissions.AllowAny]
