# -*- encoding: utf-8 -*-
from bleach import (
    clean,
    ALLOWED_TAGS,
    ALLOWED_ATTRIBUTES,
)

from django import forms
from django.forms.utils import flatatt
from django.forms.widgets import FileInput
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


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
        'table',
        'tbody',
        'td',
        'thead',
        'tr',
        'u',
    ]
    return clean(data, tags=tags, attributes=attributes, styles=styles)


def set_widget_required(field):
    """Why do I need to call this when setting 'required' on the form."""
    field.widget.attrs.update({
        'required': None,
        'placeholder': 'This is a required field',
    })
    field.required = True


class FileDropInput(FileInput):

    def __init__(self, **kwargs):
        self.default_text = kwargs.pop('default_text', "Drop a file...")
        self.click_text = kwargs.pop('click_text', "or click here...")
        super().__init__(**kwargs)

    def render(self, name, value, attrs=None):
        filedrop_class = ''
        if value is None:
            value = ''
        extra_attrs = attrs.copy() if attrs else {}
        extra_attrs.update(name=name, type=self.input_type)
        final_attrs = self.build_attrs(self.attrs, extra_attrs)
        if final_attrs:
            fd_class = final_attrs.get('class', None)
            if fd_class:
                filedrop_class = "class=\"{}\"".format(fd_class)
                del final_attrs['class']

            final_attrs['data-default-text'] = force_text(self.default_text)
            if value != '':
                # Only add the 'value' attribute if a value is non-empty.
                final_attrs['value'] = force_text(self.format_value(value))
        return mark_safe((
            '<div id="filedrop-zone" {}>'
            '<span id="filedrop-file-name">{}</span>'
            '<div id="filedrop-click-here">'
            '{}'
            '<input {}>'
            '</div>'
            '</div>'
        ).format(
            filedrop_class, self.default_text, self.click_text,
            flatatt(final_attrs)
        ))


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
            if (isinstance(f, forms.FileField) or
                    isinstance(f, forms.ImageField)):
                f.widget = FileDropInput()
