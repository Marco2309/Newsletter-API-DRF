# Generated by Django 2.2 on 2021-04-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_administrador',
            field=models.BooleanField(null=True),
        ),
    ]