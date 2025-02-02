from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='index'),
    path('search/', views.search, name='search'),
    path('product/<int:pk>/', views.product, name='product'),
]