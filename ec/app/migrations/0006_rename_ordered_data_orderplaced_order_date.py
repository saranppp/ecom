# Generated by Django 4.2 on 2023-06-04 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customer_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='ordered_data',
            new_name='order_date',
        ),
    ]
