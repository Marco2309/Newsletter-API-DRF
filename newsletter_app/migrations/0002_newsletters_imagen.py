# Generated by Django 2.2 on 2021-04-24 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletters',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
