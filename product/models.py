from django.db import models
from django.utils.translation import gettext as _
from accounts.models import CustomUser


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


class Comment(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comment",
                                 verbose_name="Username")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment", verbose_name=_("Product"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True,
                               verbose_name="Reply comment")
    massage = models.TextField(verbose_name="Massage")

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Time Created")
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name="Date Time Modified")

    def __str__(self):
        return str(self.massage)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
