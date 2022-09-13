from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import login


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_types"] = "client"
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("produtos:home")
        return super(SignUpView, self).get(request, *args, **kwargs)


class LoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("produtos:home")
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.get_user().role == "SUPERMARKET":
            login(self.request, form.get_user())
            return redirect("lojista:minhas_ordens")
        return super().form_valid(form)
