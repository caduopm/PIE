# Generated by Django 2.2.4 on 2020-06-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_animal', '0005_animal_lost_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='found_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
