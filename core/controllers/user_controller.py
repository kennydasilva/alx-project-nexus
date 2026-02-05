from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import User
from core.serializers.user_serializer import UserSerializer
from core.services.user_service import UserService

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        users = UserService.list_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.create_user(serializer.validated_data)
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )

    def retrieve(self, request, pk=None):
        user = UserService.get_user_by_id(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = UserService.get_user_by_id(pk)
        UserService.deactivate_user(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
