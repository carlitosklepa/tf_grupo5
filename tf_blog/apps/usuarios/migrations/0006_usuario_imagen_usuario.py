# Generated by Django 4.0 on 2021-12-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuario_imagen_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen_usuario',
            field=models.ImageField(null=True, upload_to='usuarios'),
        ),
    ]
