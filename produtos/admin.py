from django.contrib import admin
from .models import Categoria, Produto, Ordem, OrdemItem


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto_nome', 'preco', 'quantidade_vendida', 'quantidade_em_estoque')
    prepopulated_fields = {'slug': ("produto_nome",)}


class OrdemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user', 
        'number_order',
        'produtos',
        'enviado',
        'data_pedido',
        )
    list_display_links = ('id', 'number_order',)


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(OrdemItem)
admin.site.register(Ordem, OrdemAdmin)

