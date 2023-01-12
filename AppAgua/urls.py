"""AppAgua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from clientes.api.router import router_clientes,router_valores, router_cifras, router_cobros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(router_clientes.urls)),
    path('valores/', include(router_valores.urls)),
    path('cifras/', include(router_cifras.urls)),
    path('cobros/', include(router_cobros.urls))
]
