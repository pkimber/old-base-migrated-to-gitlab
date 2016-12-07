# -*- encoding: utf-8 -*-
from django import forms
from base.form_utils import RequiredFieldForm, FileDropInput
from .models import Document


class DocumentForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('file', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Document
        fields = (
            'file',
            'description',
        )

        # Not required RequiredFieldForm uses FileDropInput for FileField
        # widgets = {'file': FileDropInput()}


# this is an example of how to use in a basic ModelForm
class BasicDocumentModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('file', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Document
        fields = (
            'file',
            'description',
        )
        widgets = {'file': FileDropInput()}


# this is an example of how to use in a basic Form
class NonModelForm(forms.Form):

    file = forms.FileField(widget=FileDropInput)
    description = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('file', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )
