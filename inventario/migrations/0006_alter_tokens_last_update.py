# Generated by Django 4.1.5 on 2023-01-21 04:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_tokens_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 4, 2, 13, 412869, tzinfo=datetime.timezone.utc)),
        ),
    ]