# Generated by Django 4.1 on 2022-08-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('idprovedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('razonsocial', models.TextField()),
                ('ruc', models.TextField()),
                ('direccion', models.TextField()),
                ('telefono', models.TextField()),
                ('representantelegal', models.TextField()),
                ('estado', models.TextField()),
            ],
        ),
    ]