# Generated by Django 4.1.5 on 2023-01-20 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_tokens_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notas',
            field=models.CharField(db_index=True, default='NA', max_length=250),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 4, 25, 43, 760653, tzinfo=datetime.timezone.utc)),
        ),
    ]