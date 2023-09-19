from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "home.html")


def sobre_view(request):
    return render(request, "sobre.html")


def blog_view(request):
    return render(request, "blog.html")


def user_view(request, username):
    return HttpResponse(f"Nome do Usuário: {username}")


# Create your views here.
