from django.contrib import admin

# Register your models here.
from . models import Empresa,Horario


class HorarioInline(admin.StackedInline):
    model = Horario

class EmpresaAdmin(admin.ModelAdmin):
    inlines=[HorarioInline,]


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Horario)