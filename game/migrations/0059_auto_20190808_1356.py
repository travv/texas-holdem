# Generated by Django 2.2.4 on 2019-08-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0058_auto_20190808_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='turn',
            field=models.IntegerField(default=0),
        ),
    ]
