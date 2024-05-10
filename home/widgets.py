from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('Select Image')
    template_name = 'home/custom_widget_templa\
        te/custom_clearable_file_input.html'


class CustomClearableIconInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('Select Icon')
    template_name = 'home/custom_widget_templa\
        te/custom_clearable_file_input.html'
