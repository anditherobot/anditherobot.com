from django.db import models

# Create your models here.
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core import blocks


#Goes with model name
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    #only 1 homepage instance at a time
    max_count = 1
    jumbotron = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock())
    ], default=None)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
         StreamFieldPanel('jumbotron'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

#If there's 1 model you wont be able to choose. Add two or more to see the list
class GenericPage(Page):
    banner_title = models.CharField(max_length=100)
    banner_image = models.ForeignKey('wagtailimages.Image', 
    null=True, 
    blank=False, 
    on_delete=models.SET_NULL, 
    related_name='+')

    content_panels = Page.content_panels + [
         FieldPanel('banner_title'),
         ImageChooserPanel('banner_image')
    ]

class EventsPage(Page):
    banner_title =models.CharField(max_length=100)
    content_panels = Page.content_panels + [
         FieldPanel('banner_title'),
       
    ]

class EventsDetailsPage(Page):
    banner_title =models.CharField(max_length=100)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    content_panels = Page.content_panels + [
         FieldPanel('banner_title'),
         FieldPanel('begin_date'),
         FieldPanel('end_date'),
       
    ]