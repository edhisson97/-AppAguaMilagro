from django.db import models

class Cliente(models.Model):
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    medidor=models.CharField(max_length=10,unique=True)
    cedula=models.CharField(max_length=10)
    email=models.EmailField()

class ValoresBase(models.Model):
    valor_cifra_base=models.DecimalField(max_digits=30, decimal_places=2)
    valor_adicional=models.DecimalField(max_digits=30, decimal_places=2,null=True, blank=True)
    base=models.IntegerField()
    porcentaje_mora=models.IntegerField()

class Cifras(models.Model):
    id_usuario=models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    mes=models.CharField(max_length=10)
    anio=models.CharField(max_length=4)
    cifra=models.IntegerField()
    estado=models.CharField(max_length=1,default='n')

class Cobros(models.Model):
    id_usuario=models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    registro=models.DateTimeField(auto_now_add=True)
    fechacifra=models.CharField(max_length=15)
    total=models.DecimalField(max_digits=30, decimal_places=2)

    