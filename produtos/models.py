from django.db import models
from users.models import CustomUser
from django.urls import reverse



class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    produto_nome = models.CharField(max_length=70)
    preco = models.IntegerField()
    quantidade_em_estoque = models.IntegerField()
    quantidade_vendida = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(default='', blank=True, null=True)
    slug = models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return self.produto_nome

    def existe_produto_estoque(self):
        if self.quantidade_em_estoque > 0:
            return True
        return False

    def produto_vendido(self):
        if self.existe_produto_estoque():
            self.quantidade_em_estoque -= 1
            self.quantidade_vendida += 1
            return True
        return False

    def add_ao_carrinho(self):
        return reverse('produto:carrinho', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('produto:produto_detail', kwargs={'slug': self.slug})


class OrdemItem(models.Model):
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade} de {self.produto.produto_nome}'

    def get_total_item_preco(self):
        return self.quantidade * self.produto.preco


class Ordem(models.Model):
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    produtos_itens = models.ManyToManyField(OrdemItem)
    data_pedido = models.DateField()
    data_pedido_enviado = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente.username
    
    def get_total_preco(self):
        total = 0
        for pedido in self.produtos.all():
            total += pedido.get_total_item_preco()
        return total

