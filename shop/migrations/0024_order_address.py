# Generated by Django 4.2.1 on 2023-06-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_alter_order_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.address'),
            preserve_default=False,
        ),
    ]
