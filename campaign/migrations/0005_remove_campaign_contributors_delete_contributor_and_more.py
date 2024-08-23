# Generated by Django 5.0.6 on 2024-08-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_alter_campaign_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='contributors',
        ),
        migrations.DeleteModel(
            name='Contributor',
        ),
        migrations.AddField(
            model_name='campaign',
            name='contributors',
            field=models.IntegerField(default=0),
        ),
    ]