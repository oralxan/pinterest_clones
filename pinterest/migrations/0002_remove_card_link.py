# Generated by Django 4.2.8 on 2024-01-19 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='link',
        ),
    ]