# Generated by Django 4.1.7 on 2023-03-02 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='nome',
            new_name='name',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
    ]
