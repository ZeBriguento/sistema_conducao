from re import search
from django.contrib import admin
from .models import Pessoa, Funcionario, Aluno, Instrutor, Mecanico
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AlunoResource(resources.ModelResource):
    class Meta:
        model = Aluno

class FuncionarioResource(resources.ModelResource):
    class Meta:
        model = Funcionario

# Register your models here.
class FuncionarioAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['primeiro_nome', 'bi', 'sobrenome']
    list_display = ('primeiro_nome', 'contacto', 'sexo')
    resource_class = FuncionarioResource

class AlunoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['primeiro_nome', 'bi', 'sobrenome']
    list_display = ('primeiro_nome', 'contacto', 'sexo')
    resource_class = AlunoResource

class InstrutorAdmin(admin.ModelAdmin):
    search_fields = ['primeiro_nome', 'bi', 'sobrenome']
    list_display = ('primeiro_nome', 'contacto', 'sexo', 'tipo_instrutor')

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Instrutor, InstrutorAdmin)
admin.site.register(Mecanico)
