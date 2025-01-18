from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(validators=[
        MinValueValidator(100)
    ])
    image = models.ImageField(upload_to='mediafiles/', null=True)
    rate = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        
    @property
    def images(self):
        return MoreProductImage.objects.filter(product=self)
    
    @property
    def rating_range(self):
        return range(self.rate)
    
    @property
    def popularity(self):
        return PopularityVote.objects.filter(product=self).count()


class MoreProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mediafiles/', null=True)

    def __str__(self):
        return f'Image for {self.product.name}'

class PopularityVote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['product', 'user']
    
    def __str__(self):
        return f'Vote for {self.product.name} by {self.user.username}'