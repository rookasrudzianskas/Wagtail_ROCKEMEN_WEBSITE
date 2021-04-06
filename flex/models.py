from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock

from home.models import new_table_options
from streams import blocks
from wagtail.core import blocks as wagtail_blocks


class FlexPage(Page):
    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonial_block.html",
        )),
        ('pricing_table', blocks.PricingTableBlock(
            table_options=new_table_options,
        )),
        # ("richtext_with_title", blocks.RichTextWithTitleBlock()),
        ('richtext', wagtail_blocks.RichTextBlock(
           template="streams/simple_richtext_block.html",
            features=["bold", "italic", "ol", "ul", "link"],
        )),


    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Flex (misc) Page"
        verbose_name_plural = "Flex (misc) Pages"
