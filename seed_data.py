import os
import django
import sys

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from shop.models import Product

def seed():
    products = [
        {
            'name': 'Cordyceps Energy Tea',
            'price': 45.00,
            'primary': 'products/cordyceps_tea.jpg',
            'hover': 'products/cordyceps_tea.jpg',
        },
        {
            'name': 'Chaga Vitality',
            'price': 48.00,
            'primary': 'products/chaga_vitality.jpg',
            'hover': 'products/chaga_vitality.jpg',
        },
        {
            'name': 'Turkey Tail Capsules',
            'price': 42.00,
            'primary': 'products/turkey_tail.jpg',
            'hover': 'products/turkey_tail.jpg',
        },
        {
            'name': 'Lion\'s Mane Wellness',
            'price': 52.00,
            'primary': 'products/lions_mane.jpg',
            'hover': 'products/lions_mane.jpg',
        },
        {
            'name': 'Foraged Oyster Mushrooms',
            'price': 35.00,
            'primary': 'products/oyster_mushrooms.jpg',
            'hover': 'products/oyster_mushrooms.jpg',
        },
    ]

    for p in products:
        Product.objects.update_or_create(
            name=p['name'],
            defaults={
                'price': p['price'],
                'primary_image': p['primary'],
                'hover_image': p['hover']
            }
        )
    print("Marketplace updated with new GOURME products!")

if __name__ == "__main__":
    seed()
