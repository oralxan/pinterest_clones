# Generated by Django 4.2.8 on 2024-01-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='img_user',
            field=models.ImageField(upload_to='author-imgs/', verbose_name='image of the author'),
        ),
    ]