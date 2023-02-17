from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    scores = (
        ('bad', 1),
        ('not bad', 2),
        ('good', 3),
        ('great', 4),
        ('perfect', 5)
    )
    name_product = models.CharField(max_length=100, verbose_name=_("Name Product"))
    short_description = models.TextField(verbose_name=_("Short Description"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.PositiveIntegerField(verbose_name=_("Price"))
    image = models.ImageField(upload_to='ProductImage/', blank=True, verbose_name=_("Image"))
    score = models.CharField(max_length=20, choices=scores, blank=True, null=True, verbose_name=_("Score"))

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
