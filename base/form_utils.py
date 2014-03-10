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
    styles = []
    tags = ALLOWED_TAGS + ['br', 'p', ]
    return clean(data, tags=tags, attributes=attributes, styles=styles)


class RequiredFieldForm(forms.ModelForm):
    """Add the 'required' attribute"""

    def __init__(self, *args, **kwargs):
        super(RequiredFieldForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            f = self.fields[name]
            if f.required:
                f.widget.attrs.update({
                    'required': None,
                    'placeholder': 'This is a required field',
                })
            if isinstance(f, forms.DateField):
                f.widget.attrs.update({
                    'class': 'datepicker',
                })
