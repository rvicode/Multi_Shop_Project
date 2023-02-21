# Generated by Django 4.1.6 on 2023-02-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_comment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.CharField(blank=True, choices=[('Bad', '1'), ('Not Bad', '2'), ('Good', '3'), ('Very Good', '4'), ('Perfect', '5')], max_length=15, null=True, verbose_name='نمره'),
        ),
    ]
