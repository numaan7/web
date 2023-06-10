# Generated by Django 4.2.1 on 2023-05-21 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='offer',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]