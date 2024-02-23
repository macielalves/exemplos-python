# Generated by Django 5.0.2 on 2024-02-22 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_clubetime_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubetime',
            options={'verbose_name_plural': 'Clubes/Times'},
        ),
        migrations.AlterModelOptions(
            name='competicao',
            options={'verbose_name_plural': 'Competições'},
        ),
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AlterModelOptions(
            name='titulocompeticao',
            options={'verbose_name_plural': 'Título de Competições'},
        ),
        migrations.AlterField(
            model_name='clubetime',
            name='jogadores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.jogador'),
        ),
        migrations.AlterField(
            model_name='clubetime',
            name='titulos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.titulocompeticao'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='clube',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.clubetime'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='numero_camisa',
            field=models.PositiveIntegerField(default=1),
        ),
    ]