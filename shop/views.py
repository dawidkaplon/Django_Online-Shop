from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewOfferForm
from .models import Item, Cart, CartItem

# Create your views here.


def index(request):
    return render(request, 'index.html')


def error404(request):
    return render(request, 'error.html')


def category(request, category):
    sport_items = Item.objects.filter(category='Sport')
    fashion_items = Item.objects.filter(category='Fashion')
    electronics_items = Item.objects.filter(category='Electronics')
    automobile_items = Item.objects.filter(category='Automobile')

    return render(request, 'category.html',
                  {
                      'category': category, 'sport_items': sport_items, 'fashion_items': fashion_items,
                      'electronics_items': electronics_items, 'automobile_items': automobile_items
                  })


def add_offer(request):
    form = NewOfferForm()
    if request.method == 'POST':
        form = NewOfferForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            categ_num = form.cleaned_data['category']
            category = NewOfferForm.CATEGORIES[int(categ_num) - 1][1]
            image = request.FILES.get('image')
            item = Item(user=user, name=name, description=description,
                        price=price, category=category, image=image)
            print(item.image.url)
            item.save()
            return redirect(f'/offer/{item.id}')
        else:
            form = NewOfferForm()
    return render(request, 'add_offer.html', {'form': form})


def view(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST' and 'add' in request.POST:
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart(user=user, total=0, quantity=0)
            cart.save()

        cart_item = CartItem(cart=cart, item=item, quantity=1)  # You need to define CartItem model
        cart_item.save()
        return redirect('/cart/')

    return render(request, 'item_details.html', {'item': item})


@login_required
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        cart = None
        cart_items = []

    if request.method == 'POST':
        for cart_item in cart_items:
            item_name_remove = f'{cart_item.item.name}_remove'
            if item_name_remove in request.POST:
                cart_item.delete()
                return redirect('/cart/')

    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})
