from django.db import models

# Create your models here.


class Empresa(models.Model):
    nomeEmpresa = models.CharField(max_length=255)
    razaoSocial = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    endereço = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    email = models.EmailField()
    dataCadastroEmp = models.DateTimeField(auto_now_add=True)
    dataUpdateEmp = models.DateTimeField(auto_now=True)
    
