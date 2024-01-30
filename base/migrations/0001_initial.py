# Generated by Django 5.0 on 2024-01-04 06:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('amount', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Not Paid')], default='unpaid', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pay_fees', models.ManyToManyField(to='base.payfees')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=8)),
                ('age', models.PositiveIntegerField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('email', models.EmailField(max_length=120)),
                ('password', models.CharField(max_length=155, null=True)),
                ('student_number', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='Student Number')),
                ('year_level', models.PositiveIntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1, verbose_name='Year Level')),
                ('semester', models.PositiveIntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester')], default=1)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('dropped', 'Dropped'), ('completed', 'Completed')], default='active', max_length=30)),
                ('grade', models.DecimalField(blank=True, decimal_places=2, help_text="Enter the student's grade on a scale from 1.00 to 5.00.", max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('remark', models.CharField(blank=True, choices=[('passed', 'Passed'), ('failed', 'Failed'), ('inc', 'INC')], max_length=20, null=True)),
                ('eligible_years', models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1)),
                ('eligable_courses', models.ManyToManyField(to='base.course')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.instructor')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(to='base.subject'),
        ),
    ]