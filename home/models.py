from django.db import models
from django.contrib.auth.models import User

"""
Model to select the status of the Communication Status
of either Published or Draft
"""
class CommunicationStatus(models.Model):

    class Meta:
        verbose_name_plural = 'Status'
    
    status = models.CharField(max_length=254)

    def __str__(self):
        return self.status



"""
Model to select the status of the Communication Type
of either Newssletter or Website
"""
class CommunicationType(models.Model):

    class Meta:
        verbose_name_plural = 'Communication Type'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


"""
Model to store the status of the Communication Content
"""
class CommunicationContent(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacy_content')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to=u'uploads/')
    status = models.ForeignKey(CommunicationStatus, on_delete=models.SET_DEFAULT, default=1)
    content_type = models.ForeignKey(CommunicationType, on_delete=models.SET_DEFAULT, default=2)

    class Meta:
        verbose_name_plural = 'Communication Content'
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    