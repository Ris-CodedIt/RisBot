# Generated by Django 4.1.7 on 2023-03-20 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
