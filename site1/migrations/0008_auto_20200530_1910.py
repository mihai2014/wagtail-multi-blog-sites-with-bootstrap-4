# Generated by Django 3.0.6 on 2020-05-30 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0007_remove_site1home_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site1home',
            old_name='intro',
            new_name='body',
        ),
    ]