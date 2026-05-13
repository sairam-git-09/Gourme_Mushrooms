from django.contrib import admin
from .models import Product, Category, PageContent

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'hex_color')
    prepopulated_fields = {'slug': ('title',)}

class PageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PageContent, PageContentAdmin)
