from django.db import models
from django.utils import timezone
from django.utils.text import slugify



class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок блога')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Уже тут')
    views_counter = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title} '

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'