import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from shop.models import PageContent, Category

# 1. Remove duplicate pages
pages = PageContent.objects.all()
seen = set()
for p in pages:
    if p.slug in seen:
        print(f"Deleting duplicate page: {p.slug}")
        p.delete()
    else:
        seen.add(p.slug)

# 2. Add missing pages: 'extracts', 'products'
for slug in ['extracts', 'products', 'recipes']:
    PageContent.objects.get_or_create(
        slug=slug,
        defaults={
            'title': slug.replace('-', ' ').title(),
            'body_text': f'Content for {slug.replace("-", " ")} goes here.'
        }
    )

# 3. Update Categories
# First, delete old ones
Category.objects.all().delete()

# Create new ones based on landing page
categories_data = [
    {"title": "The Collection", "slug": "the-collection", "hex_color": "#8A9A5B"},
    {"title": "Essences & Elixirs", "slug": "essences-elixirs", "hex_color": "#A67B5B"},
    {"title": "Culinary & Wisdom", "slug": "culinary-wisdom", "hex_color": "#2D2D2A"},
    {"title": "The Science & Soul", "slug": "the-science-soul", "hex_color": "#D7C9B8"},
]

for c in categories_data:
    Category.objects.create(**c)

print("Database updated successfully!")
