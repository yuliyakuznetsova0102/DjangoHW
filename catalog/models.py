from django.db import models


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
    image = models.ImageField(upload_to='catalog/image', verbose_name='изображение', blank=True, null=True)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(verbose_name='дата создания')
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'category']