# Generated by Django 4.2.1 on 2023-06-05 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_offers', to='shop.offer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_seller', to='shop.seller'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.product'),
        ),
    ]
