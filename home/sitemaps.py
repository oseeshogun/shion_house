from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:home', 'about:about', 'contact:contact']

    def location(self, item):
        return reverse(item)
