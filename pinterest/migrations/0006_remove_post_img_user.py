# Generated by Django 4.2.8 on 2024-01-21 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0005_post_accounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_user',
        ),
    ]
