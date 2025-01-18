from django.db import models
from django.utils.translation import gettext_lazy as _
from meta.models import ModelMeta
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class SEOImage(models.Model):
    """Model for optimized images with SEO attributes"""
    title = models.CharField(_('Title'), max_length=200)
    alt_text = models.CharField(_('Alternative Text'), max_length=255)
    image = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFill(1200, 630)],  # Optimal size for social sharing
        format='JPEG',
        options={'quality': 85}
    )
    caption = models.CharField(_('Caption'), max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('SEO Image')
        verbose_name_plural = _('SEO Images')

    def __str__(self):
        return self.title

class SEOMixin(ModelMeta):
    """Mixin to add SEO fields to any model"""
    meta_title = models.CharField(_('Meta Title'), max_length=70, blank=True)
    meta_description = models.CharField(_('Meta Description'), max_length=160, blank=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=255, blank=True)
    og_image = models.ForeignKey(
        SEOImage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_og_image'
    )
    canonical_url = models.URLField(_('Canonical URL'), blank=True)
    
    class Meta:
        abstract = True

    def get_meta(self, request=None):
        meta = super().get_meta(request)
        meta.title = self.meta_title or str(self)
        meta.description = self.meta_description
        meta.keywords = [k.strip() for k in self.meta_keywords.split(',') if k.strip()]
        if self.og_image:
            meta.image = request.build_absolute_uri(self.og_image.image.url) if request else self.og_image.image.url
        return meta
