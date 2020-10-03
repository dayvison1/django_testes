from django.contrib import admin

# Register your models here.
from . models import Empresa,Horario,Servico,Vagas



class ServicoInline(admin.StackedInline):
    model = Servico

class HorarioInline(admin.StackedInline):
    model = Horario

class EmpresaAdmin(admin.ModelAdmin):
    inlines=[HorarioInline,]

class EmpresaAdmin(admin.ModelAdmin):
    inlines=[HorarioInline,ServicoInline]
class VagasAdmin(admin.ModelAdmin):
    list_display=('NomeCliente','telefone')

admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Servico)
admin.site.register(Horario)
admin.site.register(Vagas)
