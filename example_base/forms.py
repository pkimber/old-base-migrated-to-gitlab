# -*- encoding: utf-8 -*-
from base.form_utils import RequiredFieldForm

from .models import Document
from base.form_utils import FileDropInput


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
        widgets = {'file': FileDropInput()}
