from .models import Product
from django.core.cache import cache



def get_products_by_category(category_id):
    cache_key = f'products_category_{category_id}'
    products = cache.get(cache_key)
    if not products:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(cache_key, products, timeout=60 * 15)
    return products