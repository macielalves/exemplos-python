# Generated by Django 5.0.2 on 2024-02-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicao',
            name='tipo',
            field=models.CharField(choices=[('ESTADUAL', 'ESTADUAL'), ('NACIONAL', 'NACIONAL'), ('INTERNACIONAL', 'INTERNACIONAL')], default='ESTADUAL', max_length=13),
        ),
    ]
