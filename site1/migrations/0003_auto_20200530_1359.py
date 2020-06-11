# Generated by Django 3.0.6 on 2020-05-30 13:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('site1', '0002_auto_20200529_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site1Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'site1(tech) categories',
            },
        ),
        migrations.AddField(
            model_name='site1post',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='site1.Site1Category'),
        ),
    ]
