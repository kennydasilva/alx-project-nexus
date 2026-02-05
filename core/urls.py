from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.controllers.category_controller import CategoryViewSet
from core.controllers.product_controller import ProductViewSet
from core.controllers.user_controller import UserViewSet


router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
