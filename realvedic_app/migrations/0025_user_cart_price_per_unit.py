# Generated by Django 4.1.5 on 2023-02-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0024_rename_name_user_data_first_name_user_data_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_cart',
            name='price_per_unit',
            field=models.TextField(blank=True),
        ),
    ]
