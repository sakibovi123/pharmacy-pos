# Generated by Django 4.0.1 on 2022-01-23 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0005_alter_vendor_address_alter_vendor_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinebrand',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pharmacyapp.shop'),
        ),
    ]
