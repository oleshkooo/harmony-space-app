# Generated by Django 4.1.3 on 2022-12-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]