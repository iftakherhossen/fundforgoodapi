# Generated by Django 5.0.6 on 2024-08-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_alter_campaign_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
