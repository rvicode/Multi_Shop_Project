# Generated by Django 4.1.6 on 2023-03-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_comment_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='CategoryiImage/', verbose_name='تصاویر'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخته شده'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='massage',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.CharField(blank=True, choices=[('بد', 'بد'), ('بدک نیست', 'بدک نیست'), ('خوب', 'خوب'), ('خیلی خوب', 'خیلی خوب'), ('عالی', 'عالی')], max_length=15, null=True, verbose_name='نمره'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='category', to='product.category', verbose_name='دسته بندی'),
        ),
    ]
