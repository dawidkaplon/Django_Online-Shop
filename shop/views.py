from django.shortcuts import render, redirect
from .forms import NewOfferForm
from .models import Item

# Create your views here.

def index(request):
    return render(request, 'index.html')

def error404(request):
    return render(request, 'error.html')

def category(request, category):
    return render(request, 'category.html', {'category': category})

def add_offer(request):
    form = NewOfferForm()
    if request.method == 'POST':
        form = NewOfferForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            categ_num = form.cleaned_data['category']
            category = NewOfferForm.CATEGORIES[int(categ_num) - 1][1]
            item = Item(name=name, description=description, price=price, category=category)
            item.save()
            form = NewOfferForm()
        else:
            form = NewOfferForm()
    return render(request, 'add_offer.html', {'form': form})
