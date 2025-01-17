from django.shortcuts import render

from shop.models import Product

def index(request):
    popular_items = Product.objects.order_by('-popularity')[:4]
    arrivals = Product.objects.order_by('-created_at')[:8]
    context = {
        'popular_items': popular_items,
        'arrivals': arrivals
    }
    return render(request, 'home/index.html', context=context)