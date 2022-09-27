from django.views.generic import ListView, DetailView, View
from .models import Produto, OrdemItem, Ordem, Categoria
from .func_op_carrinho import carrinho_acoes
from users.models import Lojista

from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import date, timedelta
from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.


class HomeView(ListView):
    model = Produto
    context_object_name = "products"
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        product = request.POST.get("id")
        cart = request.session.get("cart")

        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("produtos:ordemview")        

    def get_queryset(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        g = GeoIP2()
        location = g.city(ip)['city']
        qs = super().get_queryset()
        return qs.filter(Q (expiration_date__gte=date.today() + timedelta(days=1)) & Q(supermarket__city__icontains=location))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categorias"] = Categoria.objects.all()
        return context


class ProcurarProdutoView(ListView):
    model = Produto
    template_name = "home.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("search")
        if query is not None:
            if qs.filter(name__icontains=query.strip()).exists():
                return qs.filter(name__icontains=query.strip()).order_by("name")
            else:
                messages.info(
                    self.request,
                    "Produto não encontrado. Tente novamente com outro nome!",
                )
                return qs.none()


class CategoriaProdutoView(ListView):
    model = Categoria
    template_name = "home.html"
    context_object_name = "categorias"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["products"] = Produto.objects.filter(
            Q(category__slug=self.kwargs["slug"])
            & Q(expiration_date__gte=date.today() + timedelta(days=1))
        )
        return context


class ProdutoDetail(DetailView):
    model = Produto
    template_name = "produto/produto_detail.html"
    context_object_name = "product"

    def post(self, request, *args, **kwargs):
        product = str(self.get_object().id)
        cart = request.session.get("cart")

        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("produtos:ordemview")

    def get_queryset(self):
        return Produto.objects.filter(
            expiration_date__gte=date.today() + timedelta(days=1)
        )


class CheckoutView(View):
    def get(self, request):
        try:
            product = Produto.objects.filter(
                Q(id__in=list(request.session.get("cart").keys()))
                & Q(expiration_date__gte=date.today() + timedelta(days=1))
            )
            context = {"itens": product}
            return render(request, "produto/carrinho.html", context)
        except ObjectDoesNotExist:
            return render(request, "produto/carrinho.html", {})
        except:
            return render(request, "produto/carrinho.html", {})

    def post(self, request):
        product = request.POST.get("id")
        cart = request.session.get("cart")
        op_quantity = request.POST.get("op_cart")
        del_car = request.POST.get("del_cart")

        if del_car:
            del request.session["cart"]
            return redirect("produtos:ordemview")

        if cart:
            quantity = cart.get(product)
            if quantity:
                carrinho_acoes(cart, product, quantity, op_quantity)
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart

        return redirect("produtos:ordemview")


class OrdemView(UserPassesTestMixin, LoginRequiredMixin, View):
    def get(self, request):
        # print(request.session.get('cart'))
        try:
            product = Produto.objects.filter(
                id__in=list(request.session.get("cart").keys())
            )
            # Verificar se todos os produtos pertencem a mesma loja
            if len(set(list(product.values_list("supermarket", flat=True)))) == 1:
                itens = []
                dict_ord = sorted(request.session["cart"].items())
                dict_car = {k: v for k, v in dict_ord}
                order, created = Ordem.objects.get_or_create(
                    user=request.user,
                    ordered=False,
                )

                for prod, qnt in zip(product, dict_car.values()):
                    # verifica se a qnt comprada ultrapassa a do estoque
                    if prod.qnt_stock >= (qnt + prod.sold):
                        order_item, created = OrdemItem.objects.get_or_create(
                            product=prod, order=order, quantity=qnt
                        )
                        prod.sold += qnt
                        prod.save()
                        itens.append(order_item)
                    else:
                        messages.warning(request, 'Não foi possível finalizar seu carrinho, verifique a quantidade dos itens.')
                        return redirect("produtos:ordemview")

                order.supermarket = Lojista.objects.get(
                    supermarket_id=product.values_list("supermarket", flat=True).first()
                )
                order.ordered = True
                order.save()
                del request.session["cart"]

                context = {
                    "itens": itens,
                    "order": order,
                }
                return render(request, "produto/ordemview.html", context)
            else:
                messages.warning(
                    request,
                    "Em seu carrinho há produtos de lojas diferentes. Escolha produto apenas da mesma loja!",
                )
                return redirect("produtos:ordemview")
        except ObjectDoesNotExist:
            return redirect("produtos:home")
        except Exception as e:
            print(e)
            return redirect("produtos:home")

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == "CLIENT" or self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "ERROR. Entre com um usuário CLIENT!")
        elif self.request.user.is_anonymous:
            messages.info(
                self.request, "Por favor, Faça login da sua conta ou crie uma nova!"
            )
            return redirect("login")
        return redirect("produtos:ordemview")
