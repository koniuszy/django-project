from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    """
    Home page for the Wagtail site.

    This is a simple example demonstrating Wagtail's page features.
    """
    intro = RichTextField(blank=True, help_text="Introduction text for the home page")
    body = RichTextField(blank=True, help_text="Main body content")

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"


class BlogPage(Page):
    """
    Blog page demonstrating StreamField feature.
    """
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('code', blocks.TextBlock(help_text="Code snippet")),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Blog Page"


class BlogIndexPage(Page):
    """
    Blog index page to list all blog posts.
    """
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blog_pages = self.get_children().live().order_by('-first_published_at')
        context['blog_pages'] = blog_pages
        return context

    class Meta:
        verbose_name = "Blog Index Page"
