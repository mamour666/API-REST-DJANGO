# Generated by Django 2.2.1 on 2019-06-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190601_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='singleProductPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
