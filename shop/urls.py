from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('api/products/', views.api_products, name='api_products'),
    path('api/categories/', views.api_categories, name='api_categories'),
    path('api/category/<slug:slug>/', views.api_category_detail, name='api_category_detail'),
    path('api/pages/<slug:slug>/', views.api_page_detail, name='api_page_detail'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
    path('search/', views.search_view, name='search'),
    path('contact/', views.contact_view, name='contact'),
]