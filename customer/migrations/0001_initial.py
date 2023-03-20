# Generated by Django 4.1.7 on 2023-03-17 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('account_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('title', models.CharField(max_length=60, null=True)),
                ('address', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Arrears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('GOLD', 'GOLD'), ('SILVER', 'SILVER'), ('BRONZE', 'BRONZE')], default='BRONZE', max_length=60)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
