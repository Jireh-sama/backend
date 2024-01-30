# Generated by Django 5.0 on 2024-01-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mname',
            new_name='middle_name',
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]