# Generated by Django 3.2.16 on 2023-01-13 10:58

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('antarestardata', '0002_remove_preorder_jumlah'),
    ]

    operations = [
        migrations.AddField(
            model_name='preorder',
            name='jumlah',
            field=models.IntegerField(default=django.db.models.expressions.CombinedExpression(django.db.models.expressions.F('qty'), '*', django.db.models.expressions.F('harga'))),
        ),
    ]