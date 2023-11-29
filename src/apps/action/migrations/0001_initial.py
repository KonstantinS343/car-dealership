# Generated by Django 4.2.7 on 2023-11-29 14:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('car_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCarDealership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('name', models.CharField(max_length=255, verbose_name='Название акции')),
                ('descritpion', models.TextField(verbose_name='Описание')),
                ('event_start', models.DateField(verbose_name='Дата начала')),
                ('event_end', models.DateField(verbose_name='Дата окончания')),
                (
                    'discount',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)],
                        verbose_name='Скидка',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Акция автосалона',
                'verbose_name_plural': 'Акции автосалонов',
                'db_table': 'action_car_dealerships',
            },
        ),
        migrations.CreateModel(
            name='ActionSupplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('name', models.CharField(max_length=255, verbose_name='Название акции')),
                ('descritpion', models.TextField(verbose_name='Описание')),
                ('event_start', models.DateField(verbose_name='Дата начала')),
                ('event_end', models.DateField(verbose_name='Дата окончания')),
                (
                    'discount',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)],
                        verbose_name='Скидка',
                    ),
                ),
                (
                    'car_model',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='supplier_car_model_action',
                        to='car_model.car',
                        verbose_name='Модель автомобиля',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Акция поставщика',
                'verbose_name_plural': 'Акции поставщиков',
                'db_table': 'action_suppliers',
            },
        ),
    ]
