from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _

from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='CategoryiImage/')

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Time Created")
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name="Date Time Modified")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:product_list", args=[str(self.id)])

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")


class Product(models.Model):
    scores = (
        ('bad', 1),
        ('not bad', 2),
        ('good', 3),
        ('great', 4),
        ('perfect', 5)
    )
    name_product = models.CharField(max_length=100, verbose_name=_("Name Product"))
    category = models.ManyToManyField(Category, related_name="category", verbose_name=_("Category"), null=True, blank=True)
    short_description = models.TextField(verbose_name=_("Short Description"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.PositiveIntegerField(verbose_name=_("Price"))
    image = models.ImageField(upload_to='ProductImage/', blank=True, verbose_name=_("Image"))
    score = models.CharField(max_length=20, choices=scores, blank=True, null=True, verbose_name=_("Score"))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name="Date Time Modified")

    def __str__(self):
        return self.name_product

    def get_absolute_url(self):
        return reverse("product:product_detail", args=[str(self.id)])

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class Comment(models.Model):
    SCORE_CHOICE = (
        (_('Bad'), _('Bad')),
        (_('Not Bad'), _('Not Bad')),
        (_('Good'), _('Good')),
        (_('Very Good'), _('Very Good')),
        (_('Perfect'), _('Perfect')),
    )
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comment", verbose_name="Username")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment", verbose_name=_("Product"))
    massage = models.TextField(verbose_name=_("Massage"))
    score = models.CharField(max_length=15, choices=SCORE_CHOICE, null=True, blank=True, verbose_name=_("Score"))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Time Created"))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("Date Time Modified"))

    def __str__(self):
        return str(self.massage)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
