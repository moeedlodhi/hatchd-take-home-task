# Generated by Django 3.2.12 on 2022-05-26 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('license_plate_number', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bay_number', models.CharField(choices=[('Bay1', 'Bay1'), ('Bay2', 'Bay2'), ('Bay3', 'Bay3'), ('Bay4', 'Bay4')], max_length=264)),
                ('booking_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lot.customer')),
            ],
            options={
                'unique_together': {('bay_number', 'booking_date')},
            },
        ),
    ]