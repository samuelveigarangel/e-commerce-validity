from django.views.generic import ListView, DetailView, View
from .models import Produto, OrdemItem, Ordem
from .func_op_carrinho import carrinho_acoes
from users.models import CustomUser, Lojista

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render, redirect

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

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         print(self.request.user.role)
    #     return super().get(request, *args, **kwargs)


class ProcurarProdutosList(ListView):
    model = Produto
    template_name = "home.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):

        query = self.request.GET.get("search")
        if query is not None:
            return Produto.objects.filter(name__icontains=query.strip()).order_by(
                "name"
            )
        else:
            return Produto.objects.none()


class ProdutosDetail(DetailView):
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


class OrdemView(View):
    def get(self, request):
        try:
            product = Produto.objects.filter(
                id__in=list(request.session.get("cart").keys())
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


class CheckoutView(UserPassesTestMixin, LoginRequiredMixin, View):
    def get(self, request):
        # print(request.session.get('cart'))
        try:
            product = Produto.objects.filter(
                id__in=list(request.session.get("cart").keys())
            )
            # Verificar se todos os produtos pertencem a mesma loja
            if len(set(list(product.values_list("supermarket", flat=True)))) == 1:
                dict_ord = sorted(request.session["cart"].items())
                dict_car = {k: v for k, v in dict_ord}
                order, created = Ordem.objects.get_or_create(
                    user=request.user,
                    ordered=False,
                )
                itens = []

                for prod, qnt in zip(product, dict_car.values()):
                    order_item, created = OrdemItem.objects.get_or_create(
                        product=prod, order=order, quantity=qnt
                    )
                    itens.append(order_item)

                order.supermarket = Lojista.objects.get(
                    supermarket_id=product.values_list("supermarket", flat=True).first()
                )
                order.ordered = True
                order.save()
                del request.session["cart"]

                context = {"itens": itens}
                return render(request, "produto/checkout.html", context)
            else:
                # adicionar mensagem de erro
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
            return HttpResponse("Logue como um usuário client")
        return redirect("login")
