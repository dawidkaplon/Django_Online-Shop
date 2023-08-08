from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def error404(request):
    return render(request, 'error.html')

def category(request, category):
    return render(request, 'category.html', {'category': category})

