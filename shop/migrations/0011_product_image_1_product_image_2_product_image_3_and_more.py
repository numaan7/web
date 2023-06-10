# Generated by Django 4.2.1 on 2023-06-04 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0010_rename_title_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='M', max_length=10),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.offer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]