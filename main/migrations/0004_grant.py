# Generated by Django 5.0.4 on 2024-04-14 22:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_corporation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('grant_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('grant_name', models.CharField(max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('corp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.corporation')),
            ],
        ),
    ]