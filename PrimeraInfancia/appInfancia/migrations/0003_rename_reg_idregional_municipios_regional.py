# Generated by Django 4.0.3 on 2022-03-31 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appInfancia', '0002_centrozonal_estado_municipios_estado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='municipios',
            old_name='reg_idregional',
            new_name='Regional',
        ),
    ]
