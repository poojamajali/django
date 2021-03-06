# Generated by Django 3.2.3 on 2021-05-26 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_role', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('specialisation', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('salary', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
