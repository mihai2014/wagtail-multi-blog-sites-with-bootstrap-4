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
from wagtail.core import blocks

from src.tools import  PageTree, readFile
from src.blocks import TwoColumnBlock, ThreeColumnBlock, VideoBlock, DjangoBlock

def side(context):
    Posts = Site1Index.objects.all()[0]
    blogpages = Posts.get_children().live().order_by('-first_published_at')
    context['last_posts'] = blogpages[:4]


class Site1Home(Page):
    body = RichTextField(blank=True)

    content = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('exe_htmljs', blocks.TextBlock()),
    ],null=True,blank=True)

    #content_panels = Page.content_panels + [
    #    FieldPanel('body', classname="full"),
    #    #StreamField('exe_htmljs'),
    #]

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        StreamFieldPanel('content'),
    ]



    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        side(context)
        return context

class Site1Index(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        side(context)
        return context


class Site1Tag(TaggedItemBase):
    content_object = ParentalKey(
        'Site1Post',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


@register_snippet
class Site1Category(models.Model):
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
        verbose_name_plural = 'site1(tech) categories'

class Site1Post(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
#    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=Site1Tag, blank=True)
    categories = ParentalManyToManyField('site1.Site1Category', blank=True)

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
        ('code_django', DjangoBlock()),
        #('video', VideoBlock()),
    ],null=True,blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

#    content_panels = Page.content_panels + [
#        FieldPanel('date'),
#        FieldPanel('intro'),
#        FieldPanel('body', classname="full"),
#        InlinePanel('gallery_images', label="Gallery images"),
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

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        side(context)
        return context
    

class Site1PageGalleryImage(Orderable):
    page = ParentalKey(Site1Post, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class Site1Tree(Page):
    def get_context(self, request):
        context = super().get_context(request)

        index = Site1Index.objects.filter(title='Posts')[0]
        #posts = index.get_children().live()
        #print(posts)
        #context['posts'] = posts

        html_menu = PageTree(index).html_menu
        context['menu'] = html_menu
        side(context)
        return context

class Site1Search(Page):
    def get_context(self, request):
        word = request.GET.get('key')
        context = super().get_context(request)
        s = get_search_backend()
        posts = s.search(word, Site1Post)
        context['posts'] = posts
        side(context)
        return context

class Site1QueryCategory(Page):
    def get_context(self, request):
        categoryName = request.GET.get('name')
        
        # Filter posts by category name
        rez = Site1Category.objects.filter(name=categoryName)
        
        if (len(rez) == 0):
            return
        else:
            # Update template context
            context = super().get_context(request)

            blogpages = Site1Post.objects.filter(categories=rez[0])
            context['blogpages'] = blogpages
            side(context)
            return context

        template = 'site1_index.html'

class Site1CategoryIndex(Page):
    def get_context(self, request):
        categories = Site1Category.objects.all()
        context = super().get_context(request)
        context['categories'] = categories       
        side(context)
        return context

class Site1TagIndex(Page):
    def get_context(self, request):
        context = super().get_context(request)
        tagList = []
        tags = Site1Tag.objects.all()
        #tags = Site1Tag.objects.order_by("tag")
        for tag in tags:
            if tag.tag.name not in tagList:
                tagList.append(tag.tag.name)
        tagList.sort()
        context['tags'] = tagList
        side(context)
        return context

class Site1QueryTag(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('name')
        blogpages = Site1Post.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        side(context)
        return context

#testing--------------------------------------------------------------------------
class Site1HtmlPage(Page):
    html_file = models.CharField(max_length=250, blank=True)
    #tags = ClusterTaggableManager(through=Site1Tag, blank=True)
    #categories = ParentalManyToManyField('site1.Site1Category', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('html_file', classname="full"),
        #FieldPanel('tags'),
        #FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('html_file'),
    ]

    #fileStr = readFile('/static/page/'+html_file)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        #context['fileStr'] = fileStr
        side(context)
        return context
#--------------------------------------------------------------------------------
