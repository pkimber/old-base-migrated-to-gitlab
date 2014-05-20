# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from bleach import (
    clean,
    ALLOWED_TAGS,
    ALLOWED_ATTRIBUTES,
)

from django import forms


def bleach_clean(data):
    """Use bleach to clean up html."""
    attributes = ALLOWED_ATTRIBUTES
    attributes.update({
        # link
        'a': [
            'href',
            'target',
        ],
        # YouTube
        'iframe': [
            'allowfullscreen',
            'frameborder',
            'height',
            'src',
            'width',
        ],
        # Image
        'img': [
            'alt',
            'src',
            'style',
        ],
    })
    styles = [
        'float',
        'height',
        'width',
    ]
    tags = ALLOWED_TAGS + [
        'br',
        'iframe',
        'img',
        'p',
    ]
    return clean(data, tags=tags, attributes=attributes, styles=styles)


def set_widget_required(field):
    """Why do I need to call this when setting 'required' on the form."""
    field.widget.attrs.update({
        'required': None,
        'placeholder': 'This is a required field',
    })
    field.required = True


class RequiredFieldForm(forms.ModelForm):
    """Add the 'required' attribute"""

    def __init__(self, *args, **kwargs):
        super(RequiredFieldForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            f = self.fields[name]
            if f.required:
                set_widget_required(f)
            if isinstance(f, forms.DateField):
                f.widget.attrs.update({
                    'class': 'datepicker',
                })
