# Generated by Django 4.2.2 on 2023-07-31 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0011_alter_deals_quantity_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='Quantity_ordered',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]