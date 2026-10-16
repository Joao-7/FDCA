from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("sair/", LogoutView.as_view(next_page="login"), name="logout"),
]