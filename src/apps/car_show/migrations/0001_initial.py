# Generated by Django 4.2.7 on 2023-11-17 07:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_model', '0001_initial'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDealershipSuppliersList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Поставщик автосалона',
                'verbose_name_plural': 'Поставщики автосалонов',
                'db_table': 'car_dealerships_suppliers_list',
            },
        ),
        migrations.CreateModel(
            name='CarShow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Локация')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Баланс')),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(10.0)], verbose_name='Вес')),
                ('engine_capacity', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(8.0)], verbose_name='Объем двигателя')),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Бензин'), ('Diesel', 'Дизель'), ('Electricity', 'Электричество')], verbose_name='Тип топлива')),
                ('gearbox_type', models.CharField(choices=[('Mechanical', 'Механическая'), ('Automatic', 'Автоматическая')], verbose_name='Тип коробки передач')),
                ('car_body', models.CharField(choices=[('Sedan', 'Седан'), ('Limousine', 'Лимузин'), ('Pickup truck', 'Пикап'), ('Hatchback', 'Хэтчбек'), ('Station wagon', 'Универсал'), ('Minivan', 'Минивэн'), ('Compartment', 'Купе'), ('Convertible', 'Кабриолет')], verbose_name='Тип кузова')),
            ],
            options={
                'verbose_name': 'Автосалон',
                'verbose_name_plural': 'Автосалоны',
                'db_table': 'cars_show',
            },
        ),
        migrations.CreateModel(
            name='UniqueBuyersCarDealership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unique_buyers_car_show_buyer', to='buyer.buyer', verbose_name='Покупатель')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unique_buyers_car_show', to='car_show.carshow', verbose_name='Автосалон')),
            ],
            options={
                'verbose_name': 'Уникальный клиент автосалона',
                'verbose_name_plural': 'Уникальные клиенты автосалонов',
                'db_table': 'unique_buyers_car_dealerships',
            },
        ),
        migrations.CreateModel(
            name='CarShowModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('model_amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество автомобилей')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_show_model_car_dealership', to='car_show.carshow', verbose_name='Автосалон')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_show_model_car', to='car_model.carmodel', verbose_name='Модель автомобиля')),
            ],
            options={
                'verbose_name': 'Модель автосалона',
                'verbose_name_plural': 'Модели автосалонов',
                'db_table': 'cars_show_car_models',
            },
        ),
    ]
