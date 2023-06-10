# Generated by Django 4.2.1 on 2023-05-21 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_offer_seller_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
