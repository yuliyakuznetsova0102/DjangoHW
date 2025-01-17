from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product



class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Успех успешный'))


        category, _ = Category.objects.get_or_create(name='Смартфоны', description='Мобильные устройства')

        products = [
            {'name': 'HONOR 200', 'description': 'Мобильные устройства',
             'image': '', 'price': 45000, 'category': category},
            {'name': 'HUAWEI Pura 70', 'description': 'Мобильные устройства', 'image': '',
             'price': 55000, 'category': category}
        ]
        for prod_data in products:
            prod, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'К успеху пришел ты: {prod.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Есть уже тут: {prod.name}'))
