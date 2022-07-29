from django.contrib import admin
from .models import Categoria, Produto, Ordem, OrdemItem

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto_nome', 'preco', 'quantidade_vendida', 'quantidade_em_estoque')
    prepopulated_fields = {'slug': ("produto_nome",)}


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(OrdemItem)
admin.site.register(Ordem)

