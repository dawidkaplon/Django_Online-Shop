from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("404/", views.error404, name="error"),
    path("add/", views.add_offer, name="add"),
    path("offer/<int:id>", views.view, name="view"),
    path("offer/<int:id>/edit", views.edit_offer, name="edit"),
    path("category/choose", views.category_list, name="category_list"), 
    path("category/<str:category_name>/", views.category, name='category_page'), 
    path("cart/", views.cart, name="cart"),
    path("user/<int:id>", views.user_view, name="view"),
    path("search/results", views.search_results, name="search_results")
]
