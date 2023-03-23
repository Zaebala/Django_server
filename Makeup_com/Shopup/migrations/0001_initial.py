# Generated by Django 4.1.7 on 2023-03-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand_id', models.CharField(max_length=100)),
                ('volume', models.IntegerField()),
                ('prise', models.IntegerField()),
                ('info', models.TextField()),
                ('img', models.ImageField(upload_to=None)),
            ],
        ),
    ]