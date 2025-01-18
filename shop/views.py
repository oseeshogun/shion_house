from django.shortcuts import render
from django.db.models import Q, Count
from django.utils import timezone

from cart.models import UserCart
from shop.models import Category, Product


def shop(request):
    cart_count = UserCart.objects.filter(
        user=request.user).count() if request.user.is_authenticated else 0
    product_count = Product.objects.count()
   

    one_month_ago = timezone.now() - timezone.timedelta(days=30)

    products = Product.objects.annotate(
        vote_count=Count('popularityvote',
                         filter=Q(popularityvote__created_at__gte=one_month_ago))
    ).order_by('-vote_count').all()

    if request.user.is_authenticated:
        products = Product.objects.annotate(
            vote_count=Count('popularityvote',
                             filter=Q(popularityvote__created_at__gte=one_month_ago, popularityvote__user=request.user))
        ).order_by('-vote_count').all()
    
    categories = products.values('category').distinct()
    
    price_range_query = request.GET.get('price')
    min_price, max_price = 0, 0
    if price_range_query:
        min_price, max_price = map(int, price_range_query.split(','))
        
        products = products.filter(price__range=(min_price, max_price))
    
    category_query = request.GET.get('category')
    if category_query:
        products = products.filter(category=category_query)
    
    

    context = {
        'cart_count': cart_count,
        'product_count': product_count,
        'categories': Category.objects.filter(id__in=categories),
        'products': products
    }
    return render(request, 'shop/index.html', context=context)


def search(request):
    cart_count = UserCart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    product_count = Product.objects.count()

    one_month_ago = timezone.now() - timezone.timedelta(days=30)

    search_query = request.GET.get('query')
    
    


    products = Product.objects.annotate(
        vote_count=Count('popularityvote',
                         filter=Q(popularityvote__created_at__gte=one_month_ago))
    ).order_by('-vote_count').filter(Q(name__icontains=search_query) | Q(description__icontains=search_query)).all()

    if request.user.is_authenticated:
        products = Product.objects.annotate(
            vote_count=Count('popularityvote',
                             filter=Q(popularityvote__created_at__gte=one_month_ago, popularityvote__user=request.user))
        ).order_by('-vote_count').filter(Q(name__icontains=search_query) | Q(description__icontains=search_query)).all()
        
    price_range_query = request.GET.get('price')
    min_price, max_price = 0, 0
    if price_range_query:
        min_price, max_price = map(int, price_range_query.split(','))
        
        products = products.filter(price__range=(min_price, max_price))

    categories = products.values('category').distinct()
    
    category_query = request.GET.get('category')
    if category_query:
        products = products.filter(category=category_query)

    context = {
        'cart_count': cart_count,
        'product_count': product_count,
        'categories': Category.objects.filter(id__in=categories),
        'products': products
    }
    return render(request, 'shop/index.html', context=context)


def product(request):
    return render(request, 'shop/index.html')
