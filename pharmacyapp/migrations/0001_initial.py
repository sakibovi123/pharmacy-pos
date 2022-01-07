# Generated by Django 4.0.1 on 2022-01-07 15:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('med_name', models.CharField(max_length=255)),
                ('med_image', models.ImageField(upload_to='images/')),
                ('buying_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_out_of_stock', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=255, null=True)),
                ('stock_amount', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MedicineCartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='MedicinePower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('power_amount', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('shop_name', models.CharField(max_length=255, unique=True)),
                ('shop_address1', models.TextField(blank=True, null=True)),
                ('shop_address2', models.TextField(blank=True, null=True)),
                ('shop_contact', models.CharField(max_length=255, null=True)),
                ('shop_bin_no', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_vat', models.CharField(blank=True, max_length=255, null=True)),
                ('mushak_no', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_logo', models.ImageField(null=True, upload_to='images/')),
                ('is_active', models.BooleanField(default=False, null=True)),
                ('vat_amount', models.FloatField(default=0, null=True)),
                ('show_mushak', models.BooleanField(default=False, null=True)),
                ('show_vat', models.BooleanField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('vendor_name', models.CharField(max_length=255, unique=True)),
                ('tax_id', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('zip_code', models.IntegerField(null=True)),
                ('trade_license', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.citymodel')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.countrymodel')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MedicineCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=255)),
                ('discount', models.FloatField(null=True)),
                ('amount_received', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('change', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('medicine_items', models.ManyToManyField(to='pharmacyapp.MedicineCartItems')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MedicineCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('med_cat_name', models.CharField(max_length=255)),
                ('is_active', models.CharField(blank=True, choices=[('ACTIVE', 'ACTIVE'), ('CLOSED', 'CLOSED')], max_length=255, null=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MedicineBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('med_brand_name', models.CharField(max_length=255)),
                ('med_brand_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='medicine',
            name='med_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.medicinebrand'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='med_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.medicinecategory'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='med_power',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.medicinepower'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='med_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.vendor'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.shop'),
        ),
        migrations.AddField(
            model_name='citymodel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.countrymodel'),
        ),
    ]
