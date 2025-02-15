from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Creates the "Модератор продуктов" group with necessary permissions'

    def handle(self, *args, **kwargs):
        # Создаем группу
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получаем необходимые права
        content_type = ContentType.objects.get_for_model(Product)
        unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_permission = Permission.objects.get(codename='delete_product')

        # Назначаем права группе
        moderator_group.permissions.add(unpublish_permission, delete_permission)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана с необходимыми правами.'))