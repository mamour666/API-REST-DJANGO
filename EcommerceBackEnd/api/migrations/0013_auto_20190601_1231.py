# Generated by Django 2.2.1 on 2019-06-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190601_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='singleProductPrice',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.CharField(max_length=1000),
        ),
    ]
