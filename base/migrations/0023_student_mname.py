# Generated by Django 5.0 on 2024-01-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_payfees_date_assigned_payments_date_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
