# Generated by Django 4.0.1 on 2022-01-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0009_purchasetype_purchasemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinecheckout',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]