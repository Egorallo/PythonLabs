# Generated by Django 4.2.1 on 2023-06-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0004_remove_servicepackinstance_order_servicepack_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepack',
            name='order',
        ),
        migrations.AlterField(
            model_name='servicepack',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
