# Generated by Django 4.2.1 on 2023-05-16 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 15, 18, 35, 608241, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
