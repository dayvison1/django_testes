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
    
    
    def __str__(self):
        return self.nomeEmpresa


class Servico(models.Model):
    nomeServico = models.CharField(max_length=255)
    precoServico = models.DecimalField('Preço', decimal_places=2,max_digits=8)
    fkEmpresaServico = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    def __str__(self):
        return self.nomeServico
    
class Horario(models.Model):
    hora = models.CharField(max_length=5)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    def __str__(self):
        return self.hora

listaServicos = []
l=[]
for i in Servico.objects.all():
    i=str(i)
    listaServicos.append(tuple((i,i)))




class Vagas(models.Model):
    SERVICOS=(('ca','Aaa'),('cb',"Bbb"))
    STATUS=(('Indisponível','Indisponível'),('Disponível','Disponível'),('Reservado','Reservado'))
    
    nomeCliente = models.CharField(max_length=255)
    telefoneCliente = models.CharField('telefone',max_length=255)
    servicoCliente = models.CharField(max_length=255,choices=listaServicos)
    idVaga = models.CharField(max_length=255)
    statusVaga = models.CharField(max_length=255,choices=STATUS)
    def __str__(self):
        return self.nomeCliente


