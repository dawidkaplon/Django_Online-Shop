from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error404, name='error'),
    path('add/', views.add_offer, name='add'),
    path('offer/<int:id>', views.view, name='view'),
    path('category/electronics/', views.category,
         {'category': 'electronics'}, name='electronics'),
    path('category/fashion/', views.category, {'category': 'fashion'}, name='fashion'),
    path('category/sport/', views.category, {'category': 'sport'}, name='sport'),
    path('category/automobile/', views.category,
         {'category': 'automobile'}, name='automobile'),
    path('cart/', views.cart, name='cart')
]
