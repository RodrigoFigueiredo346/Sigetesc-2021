# Generated by Django 3.2.6 on 2021-08-24 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='quant',
            new_name='quantidade',
        ),
    ]
