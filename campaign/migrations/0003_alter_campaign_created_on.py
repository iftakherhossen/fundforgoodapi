# Generated by Django 5.0.6 on 2024-08-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_alter_campaign_balance_alter_campaign_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='created_on',
            field=models.DateField(),
        ),
    ]
