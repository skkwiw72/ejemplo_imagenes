# Generated by Django 5.0.4 on 2024-04-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_usuario_contacos_enviado_usuario_mensajes_enviados'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='licencia_12meses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='licencia_3meses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='licencia_6meses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='licencia_mes',
            field=models.IntegerField(default=0),
        ),
    ]
