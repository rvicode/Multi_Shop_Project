# Generated by Django 4.1.6 on 2023-02-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_comment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=8, null=True),
        ),
    ]