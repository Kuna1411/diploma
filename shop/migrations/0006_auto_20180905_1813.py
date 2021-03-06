# Generated by Django 2.1 on 2018-09-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_ordermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ('category', 'title'), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
