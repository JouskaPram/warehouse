# Generated by Django 3.2.16 on 2023-01-13 11:06

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('antarestardata', '0007_auto_20230113_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='jumlah',
            field=models.FloatField(default=django.db.models.expressions.CombinedExpression(django.db.models.expressions.F('harga'), '*', django.db.models.expressions.F('qty'))),
        ),
    ]
