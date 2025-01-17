# Generated by Django 5.1.4 on 2025-01-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок блога')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Уже тут')),
                ('views_counter', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
