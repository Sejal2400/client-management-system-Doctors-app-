# Generated by Django 4.2.2 on 2023-07-25 14:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_enteredby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
