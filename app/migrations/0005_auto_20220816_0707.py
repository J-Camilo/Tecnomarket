# Generated by Django 3.1.2 on 2022-08-16 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220816_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='image',
        ),
    ]
