from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200) # e.g. Reishi Immunity
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    primary_image = models.ImageField(upload_to='products/', null=True, blank=True) # Studio shot
    hover_image = models.ImageField(upload_to='products/', null=True, blank=True) # Lifestyle shot

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    hex_color = models.CharField(max_length=7, default='#94A370')
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    hero_image = models.ImageField(upload_to='categories/heroes/', null=True, blank=True)
    page_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class PageContent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    hero_image = models.ImageField(upload_to='pages/heroes/', null=True, blank=True)
    sub_headline = models.CharField(max_length=300, null=True, blank=True)
    body_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Page Contents"
