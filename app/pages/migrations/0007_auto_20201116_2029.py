# Generated by Django 2.2 on 2020-11-16 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_pageconnector_origin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageconnector',
            old_name='destination',
            new_name='target',
        ),
    ]