# Generated by Django 4.2.1 on 2023-05-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
