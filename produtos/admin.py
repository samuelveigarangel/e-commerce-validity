from django.contrib import admin
from .models import Categoria, Produto, Ordem, OrdemItem


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'sold', 'qnt_stock')
    prepopulated_fields = {'slug': ("name",)}


class OrdemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user', 
        'number_order',
        'produtos',
        'ordered',
        'order_date',
        )
    list_display_links = ('id', 'number_order',)


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(OrdemItem)
admin.site.register(Ordem, OrdemAdmin)

