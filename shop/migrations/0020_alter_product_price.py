# Generated by Django 4.2.1 on 2023-06-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_offer_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(max_length=100),
        ),
    ]
