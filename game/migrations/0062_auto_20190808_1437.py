# Generated by Django 2.2.4 on 2019-08-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0061_table_turn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='turn',
        ),
        migrations.AddField(
            model_name='table',
            name='decission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='decission', to='game.Player'),
        ),
    ]
