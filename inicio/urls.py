from django.urls import path
from .views import IndexView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

app_name = 'inicio'
urlpatterns = [
    path('', login_required(IndexView.as_view()), name = 'index'),
]