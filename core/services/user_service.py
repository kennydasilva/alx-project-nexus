from core.models import User

class UserService:

    @staticmethod
    def create_user(data):
        return User.objects.create_user(**data)

    @staticmethod
    def list_users():
        return User.objects.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    def deactivate_user(user):
        user.is_active = False
        user.save()
