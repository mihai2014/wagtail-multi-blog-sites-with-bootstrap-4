# Generated by Django 3.0.6 on 2020-05-30 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site2', '0005_site2home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site2home',
            old_name='intro',
            new_name='body',
        ),
    ]
