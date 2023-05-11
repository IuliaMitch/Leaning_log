from django.shortcuts import render


def index(request):
    """Página Inicial"""
    return render(request, "learning_logs/index.html")


# Create your views here.
