# Generated by Django 2.0.9 on 2018-10-23 11:28

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('yekpay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='orderNumber',
            field=hashid_field.field.HashidField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7),
        ),
    ]
