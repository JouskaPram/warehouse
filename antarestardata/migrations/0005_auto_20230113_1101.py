# Generated by Django 3.2.16 on 2023-01-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antarestardata', '0004_alter_preorder_jumlah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='harga',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='preorder',
            name='qty',
            field=models.IntegerField(null=True),
        ),
    ]
