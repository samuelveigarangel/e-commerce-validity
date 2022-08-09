from django.views.generic import ListView
from produtos.models import Produto


# Create your views here.
class HomeView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'home.html'