# Generated by Django 5.0.4 on 2024-04-06 01:18

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_corporation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='(000)000-000', max_length=128, region=None),
        ),
    ]
