# Generated by Django 4.1.6 on 2023-02-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_datetime_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
