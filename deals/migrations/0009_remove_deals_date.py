# Generated by Django 4.2.2 on 2023-07-18 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0008_remove_deals_date_deals_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='Date',
        ),
    ]
