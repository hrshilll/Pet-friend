# Generated by Django 5.1.5 on 2025-04-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_cart_service_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
