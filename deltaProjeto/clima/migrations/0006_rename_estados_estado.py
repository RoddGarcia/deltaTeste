# Generated by Django 4.1.7 on 2023-03-03 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0005_estados_delete_cidades'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estados',
            new_name='Estado',
        ),
    ]
