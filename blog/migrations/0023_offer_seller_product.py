# Generated by Django 4.2.1 on 2023-05-21 15:38

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0022_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=1000, unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('price_off', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=1000, unique=True)),
                ('title', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images')),
                ('size', models.CharField(choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='M', max_length=10)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('description', models.CharField(max_length=200)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_categories', to='blog.categorie')),
                ('offer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='blog.offer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.seller')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
