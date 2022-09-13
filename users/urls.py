from django.urls import path
from .views import MinhasCompras

app_name = "users"

urlpatterns = [
    path("minhas-compras/", MinhasCompras.as_view(), name="minhas_compras"),
]
