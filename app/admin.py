from django.contrib import admin
from .models import Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ano', 'mes', 'nome', 'serie', 'turno', 'nivel')
    list_display_links = ('id', 'nome')
    # list_display_links = ('id', 'nome')
    # list_filter = ('nome', 'serie')
    # list_per_page = 10
    # search_fields = ('nome')
    # list_editable = ('nome', 'serie', 'turno', 'nivel')


admin.site.register(Aluno, AlunoAdmin)
