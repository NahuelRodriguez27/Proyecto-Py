# Generated by Django 5.0.7 on 2024-07-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_rename_fecha_de_entrega_entregable_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='email',
        ),
        migrations.AddField(
            model_name='profesor',
            name='especialidad',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]
