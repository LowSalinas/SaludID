# Generated by Django 2.2.5 on 2019-10-12 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondeusuarios', '0004_auto_20191010_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numid',
            name='Doctores',
        ),
        migrations.RemoveField(
            model_name='numid',
            name='Nutriologos',
        ),
        migrations.RemoveField(
            model_name='numid',
            name='Usuarios',
        ),
        migrations.DeleteModel(
            name='Doctores',
        ),
        migrations.DeleteModel(
            name='NumID',
        ),
        migrations.DeleteModel(
            name='Nutriologos',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
