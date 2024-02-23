# Generated by Django 5.0.2 on 2024-02-23 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_titulocompeticao_ano_conquista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulocompeticao',
            name='clube',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.clubetime'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='titulocompeticao',
            name='competicao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.competicao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='titulocompeticao',
            name='titulo',
            field=models.CharField(choices=[('CAMPEAO', 'Campeão'), ('VICE', 'Vice')], default='CAMPEAO', max_length=7),
        ),
    ]