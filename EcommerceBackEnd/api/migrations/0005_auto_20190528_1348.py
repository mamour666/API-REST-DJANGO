# Generated by Django 2.2.1 on 2019-05-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190528_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
    ]
