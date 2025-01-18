from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='index'),
    path('delete/<int:item_id>/', views.delete_cart_item, name='remove_from_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
]
