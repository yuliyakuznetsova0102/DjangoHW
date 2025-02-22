from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='описание категории', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание продукта', blank=True, null=True)
    image = models.ImageField(upload_to='media/photos', verbose_name='изображение', blank=True, null=True)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Владелец')

    PUBLISHED = 'published'
    UNPUBLISHED = 'unpublished'
    STATUS_CHOICES = [
        (PUBLISHED, 'Published'),
        (UNPUBLISHED, 'Unpublished'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=UNPUBLISHED)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'category']
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
        ]

    def save(self, *args, **kwargs):
        # Если продукт создается, автоматически назначаем владельца
        if not self.owner and hasattr(self, 'request'):
            self.owner = self.request.user
        super().save(*args, **kwargs)