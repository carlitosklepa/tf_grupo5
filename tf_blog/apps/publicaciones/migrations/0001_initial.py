# Generated by Django 4.0 on 2021-12-16 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=200)),
                ('resumen', models.CharField(default='', max_length=500)),
                ('Contenido', models.TextField(default='')),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_de_Edicion', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen_publicacion', models.ImageField(null=True, upload_to='publicaciones')),
            ],
        ),
    ]
