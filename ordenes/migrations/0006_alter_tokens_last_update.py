# Generated by Django 5.0 on 2024-07-30 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0005_alter_tokens_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 22, 28, 11, 614179, tzinfo=datetime.timezone.utc)),
        ),
    ]