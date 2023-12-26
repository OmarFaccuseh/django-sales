# Generated by Django 4.1.5 on 2023-01-22 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_alter_tokens_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='NA', max_length=250),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 17, 37, 29, 410237, tzinfo=datetime.timezone.utc)),
        ),
    ]