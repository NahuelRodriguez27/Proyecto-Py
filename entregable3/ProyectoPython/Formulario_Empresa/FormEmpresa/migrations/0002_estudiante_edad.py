# Generated by Django 5.0.7 on 2024-07-30 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='edad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
