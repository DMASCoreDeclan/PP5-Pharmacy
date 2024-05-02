from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Prescription
from .widgets import CustomClearableFileInput
from profiles.models import UserProfile

PX_DELIVERY = [
        ('0', 'Collection'),
        ('1', 'Delivery'),
    ]

class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['user', 'px_status', 'order_form', ]

    px_image = forms.ImageField(label='PrescriptionImage', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'



