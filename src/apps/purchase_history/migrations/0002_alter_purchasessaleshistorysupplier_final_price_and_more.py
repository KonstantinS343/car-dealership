# Generated by Django 4.2.7 on 2023-11-16 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasessaleshistorysupplier',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Итоговая цена'),
        ),
        migrations.AlterField(
            model_name='purchasessaleshistoryсarshow',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Итоговая цена'),
        ),
    ]
