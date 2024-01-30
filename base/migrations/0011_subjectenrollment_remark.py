# Generated by Django 5.0 on 2024-01-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_subjectenrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectenrollment',
            name='remark',
            field=models.CharField(blank=True, choices=[('passed', 'Passed'), ('failed', 'Failed'), ('inc', 'INC')], max_length=20, null=True),
        ),
    ]
