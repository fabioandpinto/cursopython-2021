# Generated by Django 3.2.9 on 2022-02-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20220219_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
