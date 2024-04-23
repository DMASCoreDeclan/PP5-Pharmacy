from django import forms
from .models import CommunicationContent, CommunicationType, CommunicationStatus
from .widgets import CustomClearableFileInput

class CommunicationForm(forms.ModelForm):

    class Meta: 
        model = CommunicationContent
        fields = '__all__'
        exclude = ['slug', 'author', 'content_type']

    image = forms.ImageField(label='Article Image', required=False, widget=CustomClearableFileInput)
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'
