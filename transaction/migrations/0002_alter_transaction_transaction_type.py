# Generated by Django 5.0.6 on 2024-08-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Donation', 'Donation')], max_length=10, null=True),
        ),
    ]
