from django import forms
from .models import CommunicationContent, CommunicationType
from .models import CommunicationStatus, Service, User
from .widgets import CustomClearableFileInput, CustomClearableIconInput


class CommunicationForm(forms.ModelForm):

    class Meta:
        model = CommunicationContent
        fields = '__all__'
        exclude = ['slug', ]

    image = forms.ImageField(
            label='Article Image',
            required=False,
            widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

    icon = forms.ImageField(label='Article Image',
                            required=False,
                            widget=CustomClearableIconInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'
