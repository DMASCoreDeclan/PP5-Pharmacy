from django.db import models

# Used to abbreviate content in admin panel
from django.template.defaultfilters import truncatewords
from django.contrib.auth.models import User


class CommunicationStatus(models.Model):
    """
    Model to select the status of the Communication Status
    of either Published or Draft
    """

    class Meta:
        verbose_name_plural = 'Status'

    status = models.CharField(max_length=254)

    def __str__(self):
        return self.status


class CommunicationType(models.Model):
    """
    Model to select the status of the Communication Type
    of either Newssletter or Website
    """

    class Meta:
        verbose_name_plural = 'Communication Type'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CommunicationContent(models.Model):
    """
    Model to store the status of the Communication Content
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='pharmacy_content')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(
                default='phelans-logo-high-cropped.png',
                upload_to='uploads/')
    status = models.ForeignKey(
            CommunicationStatus,
            on_delete=models.SET_DEFAULT,
            default=1)
    content_type = models.ForeignKey(
            CommunicationType,
            on_delete=models.SET_DEFAULT,
            default=2)

    class Meta:
        verbose_name_plural = 'Communication Content'
        ordering = ['-created_on']

    @property
    def short_description(self):
        """
        The article is too long in /admin.  This function
        abbreviates the article so only the first 25 words show
        """
        return truncatewords(self.content, 25)

    def __str__(self):
        return self.title


class Service(models.Model):
    """
    Model to select the status of the Communication Type
    of either Newssletter or Website
    """
    class Meta:
        verbose_name_plural = 'Services'

    author = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='service_content')
    icon = models.ImageField(null=False)
    title = models.CharField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return self.title
