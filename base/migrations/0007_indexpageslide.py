# Generated by Django 3.0.4 on 2020-04-01 05:18

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20200331_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPageSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Подзаголовок')),
                ('picture', models.ImageField(default=None, upload_to=base.models.IndexPageSlide.get_image_path, verbose_name='Фото')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Сортировать')),
            ],
            options={
                'verbose_name': 'Слайдер на главной странице',
                'verbose_name_plural': 'Слайдер на главной странице',
                'ordering': ['order'],
            },
        ),
    ]