# Generated by Django 3.2.16 on 2023-01-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antarestardata', '0005_auto_20230113_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='harga',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='preorder',
            name='qty',
            field=models.CharField(max_length=40),
        ),
    ]