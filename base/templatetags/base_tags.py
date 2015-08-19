# -*- encoding: utf-8 -*-
from django import template


register = template.Library()


@register.filter('is_checkbox_select_multiple')
def is_checkbox_select_multiple(obj):
    """Is this a checkbox select multiple field?

    Usage::

      {% if field|is_checkbox_select_multiple %}

    """
    return obj.field.widget.__class__.__name__ == 'CheckboxSelectMultiple'


@register.filter('is_file_input')
def is_file_input(obj):
    """Is this a file input field?

    Usage::

      {% if field|is_file_input %}

    """
    return obj.field.widget.__class__.__name__ == 'FileInput'


@register.filter('is_radio_select')
def is_radio_select(obj):
    """Is this a radio select field?

    Usage::

      {% if field|is_radio_select %}

    """
    return obj.field.widget.__class__.__name__ == 'RadioSelect'


@register.filter('is_select_multiple')
def is_select_multiple(obj):
    """Is this a select multiple field?

    Usage::

      {% if field|is_select_multiple %}

    """
    return obj.field.widget.__class__.__name__ == 'SelectMultiple'
