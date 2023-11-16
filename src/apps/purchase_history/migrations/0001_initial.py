# Generated by Django 4.2.7 on 2023-11-16 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_model', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('final_price', models.FloatField(verbose_name='Итоговая цена')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_car_show_buyer', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_car_show', to='car_show.carshow', verbose_name='Автосалон')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_car_show_car_model', to='car_model.carmodel', verbose_name='Модель автомобиля')),
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
                ('final_price', models.FloatField(verbose_name='Итоговая цена')),
                ('car_dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_supplier_car_show', to='car_show.carshow', verbose_name='Автосалон')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_supplier_car_model', to='car_model.carmodel', verbose_name='Модель автомобиля')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_history_supplier', to='supplier.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продажа поставщика',
                'verbose_name_plural': 'Продажи поставщиков',
                'db_table': 'purchases_history_suppliers',
            },
        ),
    ]