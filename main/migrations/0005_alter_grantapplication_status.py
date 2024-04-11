# Generated by Django 5.0.4 on 2024-04-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_grant_grantapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantapplication',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Accepted', 'ACCEPTED'), ('Rejected', 'REJECTED')], default='Pending', max_length=200),
        ),
    ]
