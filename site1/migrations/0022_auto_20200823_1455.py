# Generated by Django 3.0.6 on 2020-08-23 14:55

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0021_auto_20200819_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site1post',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('exe_htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock()), ('code_django', wagtail.core.blocks.StructBlock([('urls', wagtail.core.blocks.TextBlock()), ('views', wagtail.core.blocks.TextBlock()), ('template', wagtail.core.blocks.TextBlock())]))], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('exe_htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock()), ('code_django', wagtail.core.blocks.StructBlock([('urls', wagtail.core.blocks.TextBlock()), ('views', wagtail.core.blocks.TextBlock()), ('template', wagtail.core.blocks.TextBlock())]))], icon='arrow-right', label='Right column content'))])), ('three_columns', wagtail.core.blocks.StructBlock([('column1', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('exe_htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock()), ('code_django', wagtail.core.blocks.StructBlock([('urls', wagtail.core.blocks.TextBlock()), ('views', wagtail.core.blocks.TextBlock()), ('template', wagtail.core.blocks.TextBlock())]))], icon='arrow-right', label='Column 1')), ('column2', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('exe_htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock()), ('code_django', wagtail.core.blocks.StructBlock([('urls', wagtail.core.blocks.TextBlock()), ('views', wagtail.core.blocks.TextBlock()), ('template', wagtail.core.blocks.TextBlock())]))], icon='arrow-right', label='Column 2')), ('column3', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('exe_htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock()), ('code_django', wagtail.core.blocks.StructBlock([('urls', wagtail.core.blocks.TextBlock()), ('views', wagtail.core.blocks.TextBlock()), ('template', wagtail.core.blocks.TextBlock())]))], icon='arrow-right', label='Column 3'))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('exe_htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock()), ('code_django', wagtail.core.blocks.StructBlock([('urls', wagtail.core.blocks.TextBlock()), ('views', wagtail.core.blocks.TextBlock()), ('template', wagtail.core.blocks.TextBlock())]))], blank=True, null=True),
        ),
    ]
