import imp
from django.db import models
from users.models import CustomUser
from django.urls import reverse
from .random_number import random_number

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    produto_nome = models.CharField(max_length=70)
    preco = models.FloatField()
    quantidade_em_estoque = models.IntegerField()
    quantidade_vendida = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(default='', blank=True, null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return self.produto_nome

    def get_absolute_url(self):
        return reverse('produtos:produto_detail', kwargs={'slug': self.slug})


class Ordem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    enviado = models.BooleanField(default=False, null=True, blank=True)
    number_order = models.CharField(max_length=14, default=random_number, unique=True)

    def __str__(self):
        return f'{str(self.number_order)} - {self.user} - {self.enviado}'
    
    def produtos(self):
        return list(OrdemItem.objects.filter(ordem__id=self.id))

    @property
    def get_total_carrinho_preco(self):
        total = sum([item.get_total_item_preco for item in self.ordemitem_set.all()])
        return total
    
    @property
    def get_total_itens(self):
        total = sum([item.quantidade for item in self.ordemitem_set.all()])
        return total


class OrdemItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    ordem = models.ForeignKey(Ordem, on_delete=models.SET_NULL, blank=True, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f'{self.quantidade} unidade de {self.produto.produto_nome}'

    @property
    def get_total_item_preco(self):
        return self.quantidade * self.produto.preco