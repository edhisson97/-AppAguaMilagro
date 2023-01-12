from rest_framework.routers import DefaultRouter
from clientes.api.views import ClientesApiViewSet,ValoresApiViewSet,CifrasApiViewSet,CobrosApiViewSet

router_clientes = DefaultRouter()

router_clientes.register(prefix='clientes', basename='clientes', viewset=ClientesApiViewSet)

router_valores = DefaultRouter()

router_valores.register(prefix='valores', basename='valores', viewset=ValoresApiViewSet)

router_cifras = DefaultRouter()

router_cifras.register(prefix='cifras', basename='cifras', viewset=CifrasApiViewSet)

router_cobros = DefaultRouter()

router_cobros.register(prefix='cobros', basename='cobros', viewset=CobrosApiViewSet)
