# Generated by Django 4.0.2 on 2022-02-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_address_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(choices=[('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=256),
            preserve_default=False,
        ),
    ]
