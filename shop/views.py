from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Product, Category, PageContent

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

def shop(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def page_detail(request, slug):
    page = get_object_or_404(PageContent, slug=slug)
    return render(request, 'page_detail.html', {'page': page})

def api_products(request):
    category_slug = request.GET.get('category')
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.all()
    
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'category': p.category.title if p.category else '',
            'price': str(p.price),
            'primary_image': request.build_absolute_uri(p.primary_image.url) if p.primary_image else '',
            'hover_image': request.build_absolute_uri(p.hover_image.url) if p.hover_image else '',
        })
    return JsonResponse(data, safe=False)

def api_categories(request):
    categories = Category.objects.all()
    data = []
    for c in categories:
        data.append({
            'id': c.id,
            'slug': c.slug,
            'title': c.title,
            'hex_color': c.hex_color,
            'image': request.build_absolute_uri(c.image.url) if c.image else '',
        })
    return JsonResponse(data, safe=False)

def api_category_detail(request, slug):
    try:
        c = Category.objects.get(slug=slug)
        data = {
            'id': c.id,
            'slug': c.slug,
            'title': c.title,
            'page_description': c.page_description,
            'hero_image': request.build_absolute_uri(c.hero_image.url) if c.hero_image else '',
            'hex_color': c.hex_color,
        }
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def api_page_detail(request, slug):
    try:
        p = PageContent.objects.get(slug=slug)
        data = {
            'id': p.id,
            'slug': p.slug,
            'title': p.title,
            'sub_headline': p.sub_headline,
            'body_text': p.body_text,
            'hero_image': request.build_absolute_uri(p.hero_image.url) if p.hero_image else '',
        }
        return JsonResponse(data)
    except PageContent.DoesNotExist:
        return JsonResponse({'error': 'Page not found'}, status=404)

def search_view(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    
    if query:
        # Perform case-insensitive OR search across product name, category title, and category description
        search_query = Q(name__icontains=query) | \
                       Q(category__title__icontains=query) | \
                       Q(category__page_description__icontains=query)
        products = products.filter(search_query)
    
    # Categories are included in context, though not strictly necessary for search results page itself
    categories = Category.objects.all() 
    return render(request, 'search_results.html', {'products': products, 'query': query, 'categories': categories})