from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django import forms
from wagtail.contrib.table_block.blocks import TableBlock


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class LinkValue(blocks.StructValue):
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_page")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""


from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default='More details'
    )

    internal_page = blocks.PageChooserBlock(
        required=False
    )

    external_link = blocks.URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_page = value.get("external_page")
        errors = {}
        if internal_page and external_page:
            errors["internal_page"] = ErrorList(["Both of these fields cannot be filled up!. Please select only one option"])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled up!. Please select only one option"])

        elif not internal_page and not external_page:
            errors["internal_page"] = ErrorList(
                ["Please select one of the options option"])
            errors["external_link"] = ErrorList(
                ["Please select one of the options option"])
        if errors:
            raise ValidationError("Validation error in your Link", params=errors)

        return super().clean(value)


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card. Max length of 100 characters.",
    )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional text for this card. Max length is 255 characters.",
        required=False
    )
    image = ImageChooserBlock(
        help_text="Image will be automagically cropped 570px by 370px"
    )

    link = Link(help_text="Enter the link or selected a page")


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )


class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text="Image the automagically cropped to 786px by 552px")
    image_alignment = RadioSelectBlock(
        choices=(
            ("left", "Image to the Left"),
            ("right", "Image to the Right"),
        ),
        default='left',
        help_text='Image on the left with the text on the right. Or image on the right with the text on the left.'
    )
    title = blocks.CharBlock(max_length=60, help_text="Max length of 60 characters")
    text = blocks.CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"


class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, help_text='Max length of 200 characters')
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"
        icon = "plus"
        label = "Call to Action!"


class PricingTableBlock(TableBlock):
    class Meta:
        # template = 'steams/pricing_table_block.html'
        label = "Pricing Table"
        icon = "table"
        help_text = "Your pricing tables should always have minimum 4 columns"
