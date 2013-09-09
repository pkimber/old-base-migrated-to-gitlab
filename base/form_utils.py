from django import forms


class RequiredFieldForm(forms.ModelForm):
    """Add the 'required' attribute"""

    def __init__(self, *args, **kwargs):
        super(RequiredFieldForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            if self.fields[name].required:
                self.fields[name].widget.attrs.update({
                    'required': None,
                    'placeholder': 'This is a required field',
                })
