from django.forms.widgets import ClearableFileInput, NumberInput
from django.utils.translation import gettext_lazy as _


# Original from: https://github.com/django/django/blob/main/django/forms/widgets.py # noqa
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = \
        'prescription/custom_widget_template/custom_clearable_file_input.html'
