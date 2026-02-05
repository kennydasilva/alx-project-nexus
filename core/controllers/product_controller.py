from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import Product
from core.serializers.product_serializer import ProductSerializer
from core.services.product_service import ProductService

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = ProductService.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = ProductService.create_product(serializer.validated_data)
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated = ProductService.update_product(product, serializer.validated_data)
        return Response(ProductSerializer(updated).data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        ProductService.delete_product(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
