# Generated by Django 4.1.7 on 2023-03-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shine',
            name='img',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
