# Generated by Django 3.2.13 on 2023-09-08 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('regnum', models.CharField(max_length=60)),
                ('phno', models.PositiveIntegerField()),
                ('rmnum', models.PositiveIntegerField()),
                ('problem', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('created_time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
