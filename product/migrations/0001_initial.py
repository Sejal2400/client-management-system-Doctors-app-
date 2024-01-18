# Generated by Django 4.2.2 on 2023-07-02 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Company_name', models.CharField(max_length=100)),
                ('Product_image', models.ImageField(upload_to='media')),
                ('Product_price', models.FloatField()),
                ('Enteredby', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
            ],
        ),
    ]
