from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Category

class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated_at

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('shop:product_list_by_category', args=[obj.slug])
