from django.urls import path
from .views import MinhasCompras, Perfil

app_name = "users"

urlpatterns = [
    path("minhas-compras/", MinhasCompras.as_view(), name="minhas_compras"),
    path("dados/<int:pk>/", Perfil.as_view(), name="perfil"),
]
