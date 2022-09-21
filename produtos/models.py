from django.db import models
from users.models import CustomUser, Lojista
from django.urls import reverse
from .random_number import random_number
from django.utils.text import slugify
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Categoria(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produtos:categoria", kwargs={"slug": self.slug})


pre_save.connect(slug_generator, sender=Categoria)


class Produto(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    qnt_stock = models.IntegerField()
    sold = models.IntegerField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=False, null=False)
    expiration_date = models.DateField(null=True, blank=True)
    supermarket = models.ForeignKey(
        Lojista,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["expiration_date"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produtos:produto_detail", kwargs={"slug": self.slug})


pre_save.connect(slug_generator, sender=Produto)


class Ordem(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ordered = models.BooleanField(default=False, null=True, blank=True)
    number_order = models.CharField(max_length=14, default=random_number, unique=True)
    supermarket = models.ForeignKey(
        Lojista, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{str(self.number_order)} - {self.user} - {self.ordered}"

    def produtos(self):
        return list(OrdemItem.objects.filter(order__id=self.id))

    @property
    def get_total_carrinho_preco(self):
        total = sum([item.get_total_item_preco for item in self.ordemitem_set.all()])
        return total

    @property
    def get_total_itens(self):
        total = sum([item.quantity for item in self.ordemitem_set.all()])
        return total


class OrdemItem(models.Model):
    product = models.ForeignKey(
        Produto, on_delete=models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey(Ordem, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} unidade de {self.product}"

    @property
    def get_total_item_preco(self):
        return self.quantity * self.product.price
