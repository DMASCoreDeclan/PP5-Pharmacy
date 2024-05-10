from django import forms
from .models import Product, Category, ProductBundle
from .widgets import CustomClearableFileInput, RatingInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'category',
            'brand',
            'name',
            'description',
            'has_sizes',
            'size',
            'price',
            'rating',
            'thumbnail',
        )

    thumbnail = forms.ImageField(label='Product Image',
                                 required=False,
                                 widget=CustomClearableFileInput)
    rating = forms.DecimalField(
        label='Rating',
        required=False,
        widget=RatingInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-purple rounded-0'
