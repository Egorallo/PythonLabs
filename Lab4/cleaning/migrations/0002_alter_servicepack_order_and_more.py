# Generated by Django 4.2.1 on 2023-06-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepack',
            name='order',
            field=models.ManyToManyField(blank=True, to='cleaning.order'),
        ),
        migrations.AlterField(
            model_name='servicepackinstance',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]