# Generated by Django 4.2.1 on 2023-06-05 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0010_remove_servicepack_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepackinstance',
            name='service_pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cleaning.servicepack'),
        ),
    ]