from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error404, name='error'),
    path('add/', views.add_offer, name='add'),
    path('offer/<int:id>', views.view, name='view'),
    path('electronics/', views.category, {'category': 'electronics'}, name='electronics'),
    path('fashion/', views.category, {'category': 'fashion'}, name='fashion'),
    path('sport/', views.category, {'category': 'sport'}, name='sport'),
    path('automobile/', views.category, {'category': 'automobile'}, name='automobile'),
]
