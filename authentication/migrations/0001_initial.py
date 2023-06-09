# Generated by Django 4.2.1 on 2023-05-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RESTAURANT_NAME', models.CharField(max_length=100)),
                ('RESTAURANT_LOCATION', models.CharField(max_length=100)),
                ('RATING', models.IntegerField()),
                ('CUISINE_TYPE', models.CharField(max_length=100)),
                ('RESTAURANT_IMAGE', models.ImageField(upload_to=None)),
                ('RESTAURANT_STATUS', models.CharField(max_length=20)),
            ],
        ),
    ]
