# https://stackoverflow.com/questions/75791220/how-to-retrieve-value-from-dictionary-with-dynamic-key-in-django-template # noqa
'''
This templates tag translates the Tuples key and Tuple Value in tuples: 
PX_STATUS and PX_DELIVERY from the Prescrition model so that the human 
readable value is presented to the user in px_admin.html using templates tags
{% load px_options %}
'''

from django import template

# import the model with the tuples
from prescription.models import Prescription

register = template.Library()

px_status = dict(Prescription.PX_STATUS)
@register.filter(name='get_from_px_status') 
def get_from_px_status (key):
    return px_status.get(key, None)

px_delivery = dict(Prescription.PX_DELIVERY)
@register.filter(name='get_from_px_delivery') 
def get_from_px_delivery (key):
    return px_delivery.get(key, None)