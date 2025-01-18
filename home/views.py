from django.db.models import Count, Q
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from cart.models import UserCart
from shop.models import Product


def index(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    popular_items = Product.objects.annotate(
        vote_count=Count('popularityvote',
                         filter=Q(popularityvote__created_at__gte=one_month_ago))
    ).order_by('-vote_count')[:4]
    arrivals = Product.objects.order_by('-created_at')[:8]
    cart_count = UserCart.objects.filter(user=request.user).count()
    context = {
        'popular_items': popular_items,
        'arrivals': arrivals,
        'cart_count': cart_count
    }
    return render(request, 'home/index.html', context=context)
