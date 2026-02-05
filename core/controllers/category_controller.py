from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import Category
from core.serializers.category_serializer import CategorySerializer
from core.services.category_service import CategoryService

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        categories = CategoryService.list_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = CategoryService.create_category(serializer.validated_data)
        return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated = CategoryService.update_category(category, serializer.validated_data)
        return Response(CategorySerializer(updated).data)

    def destroy(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        CategoryService.delete_category(category)
        return Response(status=status.HTTP_204_NO_CONTENT)
