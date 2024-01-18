# Generated by Django 4.2.2 on 2023-10-31 06:21

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_alter_appointment_enteredby_alter_doctor_enteredby'),
        ('product', '0007_alter_product_enteredby'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0012_alter_deals_quantity_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='Date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today)]),
        ),
        migrations.AlterField(
            model_name='deals',
            name='Doctor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='deals',
            name='Enteredby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='deals',
            name='Product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]