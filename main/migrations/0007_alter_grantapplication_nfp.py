# Generated by Django 5.0.4 on 2024-04-16 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantapplication',
            name='nfp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
