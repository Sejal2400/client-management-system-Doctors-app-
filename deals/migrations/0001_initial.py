# Generated by Django 4.2.2 on 2023-07-02 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('product', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity_ordered', models.IntegerField()),
                ('Price_per_item', models.FloatField()),
                ('Total', models.FloatField()),
                ('Doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctor')),
                ('Enteredby', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
                ('Product_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
    ]