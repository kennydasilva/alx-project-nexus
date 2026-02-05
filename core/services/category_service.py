from core.models import Category

class CategoryService:

    @staticmethod
    def list_categories():
        return Category.objects.filter(is_active=True)

    @staticmethod
    def create_category(data):
        return Category.objects.create(**data)

    @staticmethod
    def update_category(instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_category(instance):
        instance.is_active = False
        instance.save()
