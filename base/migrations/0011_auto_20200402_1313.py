# Generated by Django 3.0.4 on 2020-04-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20200402_1302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpageimg',
            options={'ordering': ['order'], 'verbose_name': 'Лого', 'verbose_name_plural': 'Лого'},
        ),
        migrations.AlterModelOptions(
            name='aboutpagetext',
            options={'ordering': ['order'], 'verbose_name': 'О компании', 'verbose_name_plural': 'О компании'},
        ),
    ]
