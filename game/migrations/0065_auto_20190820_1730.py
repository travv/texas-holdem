# Generated by Django 2.2.4 on 2019-08-20 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0064_auto_20190820_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='username',
            new_name='name',
        ),
    ]
