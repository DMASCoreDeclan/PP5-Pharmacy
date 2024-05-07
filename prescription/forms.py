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

class PxForm(forms.ModelForm):
    '''
    Form for px_order.html - to allow Users to input their details and upload 
    an image file representing their PX from their
    ''' 
    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['user', 'px_status', ]

    px_image = forms.ImageField(
        label='PrescriptionImage', 
        required=True, 
        widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'


class PxAdminForm(forms.ModelForm):
    '''
    Form for px_admin.html - to allow the Pharmacy Team to review PXs to be 
    prepared
    ''' 

    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['user', 'px_status', 'order_form', ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-purple rounded-0'


class PxChangeStatusForm(forms.ModelForm):
    '''
    Form for edit_px_status.html - to allow The Paharmacy Team to view the PX 
    and update the PX Order Status
    ''' 
    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = [
            'user',
            'px_delivery',
            'px_image', 
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'