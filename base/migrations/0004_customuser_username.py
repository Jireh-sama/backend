# Generated by Django 5.0 on 2024-01-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]