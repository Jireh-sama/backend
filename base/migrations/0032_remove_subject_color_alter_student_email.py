# Generated by Django 5.0 on 2024-01-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_student_id_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='color',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=120, unique=True),
        ),
    ]
