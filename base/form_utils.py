# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from bleach import (
    clean,
    ALLOWED_TAGS,
    ALLOWED_ATTRIBUTES,
)

from django import forms
from django.contrib.auth.models import User


def bleach_clean(data):
    """Use bleach to clean up html."""
    attributes = ALLOWED_ATTRIBUTES
    attributes.update({
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


class UserCreationForm(RequiredFieldForm):
    """Copied from Django, 'UserCreationForm'.

    Designed to be used with a model derived from 'AbstractBaseUser'.
    'Meta', 'fields' should include 'password1' and 'password2'.

    """

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )

    def clean_username(self):
        """Clean the user name - check it doesn't already exist.

        Derived classes should call this method to get the 'username' before
        adding their own validation.

        """
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError(
                "A user with that username already exists."
            )
        except User.DoesNotExist:
            pass
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The two password fields didn't match."
            )
        return password2

    def save(self, commit=True):
        app = super(UserCreationForm, self).save(commit=False)
        app.set_password(self.cleaned_data["password1"])
        if commit:
            app.save()
        return app
