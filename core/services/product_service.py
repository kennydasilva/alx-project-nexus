from linecache import cache
from core.models import Product

class ProductService:

    @staticmethod
    def list_products():
        products = cache.get("products_list")
        if not products:
            products = Product.objects.filter(is_active=True)
            cache.set("products_list", products, timeout=60 * 5)
        return products

    @staticmethod
    def create_product(data):
        return Product.objects.create(**data)

    @staticmethod
    def update_product(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_product(instance):
        instance.is_active = False
        instance.save()
