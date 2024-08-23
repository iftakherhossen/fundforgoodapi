# Generated by Django 5.0.6 on 2024-08-18 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('balance_after_transaction', models.IntegerField()),
                ('transaction_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Donate', 'Donate')], max_length=10, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to='user.usermodel')),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_details', to='campaign.campaign')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
