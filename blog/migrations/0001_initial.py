# Generated by Django 4.2.3 on 2023-08-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('subtitulo', models.CharField(max_length=256)),
                ('cuerpo', models.CharField(max_length=256)),
                ('autor', models.CharField(max_length=256)),
                ('fecha', models.DateField(null=True)),
            ],
        ),
    ]