# Generated by Django 4.1 on 2022-08-26 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamiliarApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fechaCreacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]