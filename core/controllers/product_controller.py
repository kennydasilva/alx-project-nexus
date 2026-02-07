from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from core.models import Product
from core.serializers.product_serializer import ProductSerializer
from core.services.product_service import ProductService
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from core.filters import ProductFilter
from core.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ["price", "created_at"]

    serializer_class = ProductSerializer


    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsAdmin()]
        return super().get_permissions()

    def list(self, request):
        products = ProductService.list_products()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

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
