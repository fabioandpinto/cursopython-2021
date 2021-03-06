# Generated by Django 3.2.9 on 2022-02-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='persona',
            name='last_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='persona',
            name='position',
            field=models.CharField(choices=[('Directivo', 'Directivo'), ('Asesor', 'Asesor'), ('Operativo', 'Operativo'), ('Asistencial', 'Asistencial'), ('Tecnico', 'Tecnico')], max_length=50),
        ),
    ]
