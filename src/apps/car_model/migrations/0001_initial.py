# Generated by Django 4.2.7 on 2023-11-29 14:17

import django.core.validators
from django.db import migrations, models
import uuid
from typing import List


class Migration(migrations.Migration):
    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('brand', models.CharField(max_length=255, verbose_name='Марка')),
                (
                    'weight',
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(10.0)], verbose_name='Вес'
                    ),
                ),
                (
                    'engine_capacity',
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(8.0)],
                        verbose_name='Объем двигателя',
                    ),
                ),
                (
                    'fuel_type',
                    models.CharField(choices=[('Petrol', 'Бензин'), ('Diesel', 'Дизель'), ('Electricity', 'Электричество')], verbose_name='Тип топлива'),
                ),
                (
                    'gearbox_type',
                    models.CharField(choices=[('Mechanical', 'Механическая'), ('Automatic', 'Автоматическая')], verbose_name='Тип коробки передач'),
                ),
                (
                    'car_body',
                    models.CharField(
                        choices=[
                            ('Sedan', 'Седан'),
                            ('Limousine', 'Лимузин'),
                            ('Pickup truck', 'Пикап'),
                            ('Hatchback', 'Хэтчбек'),
                            ('Station wagon', 'Универсал'),
                            ('Minivan', 'Минивэн'),
                            ('Compartment', 'Купе'),
                            ('Convertible', 'Кабриолет'),
                        ],
                        verbose_name='Тип кузова',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Модель автомобиля',
                'verbose_name_plural': 'Модели автомобилей',
                'db_table': 'car_models',
            },
        ),
    ]
