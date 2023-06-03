from django.db import models
from django.utils.translation import gettext_lazy as _
from language.models import Language

class CarouselSlide(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Title'))
    content = models.TextField(null=True, blank=True, verbose_name=_('Content'))
    image = models.ImageField(upload_to='carousel_images/', verbose_name=_('Image'))
    button_text = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Button Text'))
    button_link = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Button Link'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='carousel_slides', verbose_name=_('Language'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = _('Carousel Slide')
        verbose_name_plural = _('Carousel Slides')

class MarketingItem(models.Model):
    heading = models.CharField(max_length=100, verbose_name=_('Heading'))
    content = models.TextField(verbose_name=_('Content'))
    image = models.ImageField(upload_to='marketing_images/', verbose_name=_('Image'))
    button_text = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Button Text'))
    button_link = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Button Link'))
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='marketing_items', verbose_name=_('Language'))

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = _('Marketing Item')
        verbose_name_plural = _('Marketing Items')

class Featurette(models.Model):
    heading = models.CharField(max_length=200, verbose_name=_('Heading'))
    subheading = models.CharField(max_length=200, verbose_name=_('Subheading'))
    content = models.TextField(verbose_name=_('Content'))
    image = models.ImageField(upload_to='featurette_images/', verbose_name=_('Image'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='featurettes', verbose_name=_('Language'))

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['order']
        verbose_name = _('Featurette')
        verbose_name_plural = _('Featurettes')
