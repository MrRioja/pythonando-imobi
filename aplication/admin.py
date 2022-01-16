from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Horario, DiasVisita, Imovel, Imagem, Cidade, Visitas

admin.site.disable_action('delete_selected')


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')


admin.site.register(Imagem)

admin.site.register(Cidade)

admin.site.register(Horario)

admin.site.register(DiasVisita)


@admin.action(description='Alterar status para "Agendado"')
def make_published(self, request, queryset):
    updated = queryset.update(status='p')
    self.message_user(request, ngettext(
        '%d visita foi marcada com sucesso como agendada.',
        '%d visitas foram marcadas com sucesso como agendadas.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(Visitas)
class VisitasAdmin(admin.ModelAdmin):
    list_display = ['imovel', 'usuario', 'dia', 'horario', 'status']
    list_editable = ['status']
    list_filter = ['usuario', 'imovel', 'dia', 'status']
    actions = [make_published]
