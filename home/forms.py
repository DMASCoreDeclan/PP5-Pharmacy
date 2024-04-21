from django import forms
from .models import CommunicationContent, CommunicationType, CommunicationStatus
from products.widgets import CustomClearableFileInput

class CommunicationForm(forms.ModelForm):

    class Meta: 
        model = CommunicationContent
        # fields = '__all__'
        fields= ('author', 'status', 'content_type', 'title', 'content')

    image = forms.ImageField(label='Article Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # status = CommunicationStatus.objects.all()
        # type = CommunicationType.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # self.fields['status'].choices = status
        # self.fields['content_type'].choices = type
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-1'
