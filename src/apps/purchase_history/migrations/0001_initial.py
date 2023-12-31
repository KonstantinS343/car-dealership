# Generated by Django 4.2.7 on 2023-11-29 14:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('car_model', '0001_initial'),
        ('buyer', '0002_initial'),
        ('supplier', '0001_initial'),
        ('car_show', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasesSalesHistoryСarShow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                (
                    'final_price',
                    models.DecimalField(
                        decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Итоговая цена'
                    ),
                ),
                (
                    'buyer',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='purchases_history_car_show_buyer',
                        to='buyer.buyer',
                        verbose_name='Покупатель',
                    ),
                ),
                (
                    'car_dealership',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_car_show', to='car_show.carshow', verbose_name='Автосалон'
                    ),
                ),
                (
                    'car_model',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='purchases_history_car_show_car_model',
                        to='car_model.car',
                        verbose_name='Модель автомобиля',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Продажа автосалона',
                'verbose_name_plural': 'Продажи автосалонов',
                'db_table': 'purchases_history_car_shows',
            },
        ),
        migrations.CreateModel(
            name='PurchasesSalesHistorySupplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                (
                    'final_price',
                    models.DecimalField(
                        decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Итоговая цена'
                    ),
                ),
                (
                    'car_dealership',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='purchases_history_supplier_car_show',
                        to='car_show.carshow',
                        verbose_name='Автосалон',
                    ),
                ),
                (
                    'car_model',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='purchases_history_supplier_car_model',
                        to='car_model.car',
                        verbose_name='Модель автомобиля',
                    ),
                ),
                (
                    'supplier',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_supplier', to='supplier.supplier', verbose_name='Поставщик'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Продажа поставщика',
                'verbose_name_plural': 'Продажи поставщиков',
                'db_table': 'purchases_history_suppliers',
            },
        ),
    ]
