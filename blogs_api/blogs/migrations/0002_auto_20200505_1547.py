# Generated by Django 3.0.3 on 2020-05-05 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='img',
            new_name='Image',
        ),
    ]
