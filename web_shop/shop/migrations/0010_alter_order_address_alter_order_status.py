# Generated by Django 4.0.2 on 2022-02-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
