# Generated by Django 4.1.7 on 2024-01-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_bit_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bit',
            name='bitter_address',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bit',
            name='farmer_address',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
