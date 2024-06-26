from django.db import models


# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
            max_digits=6,
            decimal_places=2,
            blank=True,
            null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    large_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_product_list(self):
        try:
            product_bundle = ProductBundle.objects.get(name=self.name)
            return product_bundle.product_list.all()
        except:
            return []


class ProductBundle(Product):
    """
    This model allows the Administrator to take two or more
    products and put them together as a SPECIAL when bought
    together
    """
    product_list = models.ManyToManyField(
        'Product', related_name='product_list'
        )

    class Meta:
        verbose_name_plural = 'Product Bundles'
