from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["massage"]
        widgets = {
            "massage": forms.Textarea(attrs={'placeholder': 'form-group'})
        }
        labels = {
            "massage": _("Message"),
        }
