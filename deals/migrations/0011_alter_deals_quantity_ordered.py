# Generated by Django 4.2.2 on 2023-07-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0010_deals_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='Quantity_ordered',
            field=models.PositiveIntegerField(),
        ),
    ]
