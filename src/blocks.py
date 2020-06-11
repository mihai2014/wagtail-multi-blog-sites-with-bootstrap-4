from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class ColumnBlock(blocks.StreamBlock):

    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    htmljs = blocks.TextBlock()
    code_bash = blocks.TextBlock()
    code_py = blocks.TextBlock()
    code_htmljs = blocks.TextBlock()

    class Meta:
        template = 'src/blocks/column.html'

class TwoColumnBlock(blocks.StructBlock):

    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'src/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

class ThreeColumnBlock(blocks.StructBlock):
    column1 = ColumnBlock(icon='arrow-right', label='Column 1')
    column2 = ColumnBlock(icon='arrow-right', label='Column 2')
    column3 = ColumnBlock(icon='arrow-right', label='Column 3')

    class Meta:
        template = 'src/blocks/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'


class VideoBlock(blocks.StructBlock):
    """video link?"""
    video = EmbedBlock() 

    class Meta:
        template = "src/blocks/video_block.html"
        icon = "media"
        label = "Embed Video"       

