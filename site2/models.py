from django.db import models

# Create your models here.

from django import forms
from django.db import models

# Create your models here.

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.search.backends import get_search_backend

from wagtail.snippets.models import register_snippet

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from src.tools import  PageTree
from src.blocks import TwoColumnBlock, ThreeColumnBlock


class Site2Home(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
    
class Site2Index(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class Site2Tag(TaggedItemBase):
    content_object = ParentalKey(
        'Site2Post',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

@register_snippet
class Site2Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'site2(blog) categories'


class Site2NewPost(Page):
    body = StreamField([
        ('exe_htmljs', blocks.TextBlock()),
    ],null=True,blank=True)
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

#from wagtail.contrib.forms.models import AbstractForm
#class FormPage(AbstractForm):
#    pass

class Site2Post(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
#    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=Site2Tag, blank=True)
    categories = ParentalManyToManyField('site2.Site2Category', blank=True)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('image', ImageChooserBlock()),
        ('exe_htmljs', blocks.TextBlock()),
        ('code_bash', blocks.TextBlock()),
        ('code_py', blocks.TextBlock()),
        ('code_htmljs', blocks.TextBlock()),
    ],null=True,blank=True)
 
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

#    content_panels = Page.content_panels + [
#        FieldPanel('date'),
#        FieldPanel('intro'),
#        FieldPanel('body', classname="full"),
##        InlinePanel('gallery_images', label="Gallery images"),
#    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        #FieldPanel('body'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class Site2PageGalleryImage(Orderable):
    page = ParentalKey(Site2Post, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


#class Site2Tree(Page):
#    pass

class Site2Search(Page):
    def get_context(self, request):
        word = request.GET.get('key')
        context = super().get_context(request)
        s = get_search_backend()
        posts = s.search(word, Site2Post)
        context['posts'] = posts
        return context


class Site2QueryCategory(Page):
    def get_context(self, request):
        categoryName = request.GET.get('name')

        # Filter posts by category name
        rez = Site2Category.objects.filter(name=categoryName)

        if (len(rez) == 0):
            return
        else:
            # Update template context
            context = super().get_context(request)

            blogpages = Site2Post.objects.filter(categories=rez[0])
            context['blogpages'] = blogpages
            return context


class Site2CategoryIndex(Page):
    def get_context(self, request):
        categories = Site2Category.objects.all()
        context = super().get_context(request)
        context['categories'] = categories
        return context


class Site2TagIndex(Page):

    def get_context(self, request):
        context = super().get_context(request)
        tagList = []
        tags = Site2Tag.objects.all()
        #tags = Site1Tag.objects.order_by("tag")
        for tag in tags:
            if tag.tag.name not in tagList:
                tagList.append(tag.tag.name)
        tagList.sort()
        context['tags'] = tagList
        return context


class Site2QueryTag(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('name')
        blogpages = Site2Post.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        #SetContext(context)
        return context

