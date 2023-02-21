from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment

SCORE_CHOICE = (
    (_('Bad'), _('Bad')),
    (_('Not Bad'), _('Not Bad')),
    (_('Good'), _('Good')),
    (_('Very Good'), _('Very Good')),
    (_('Perfect'), _('Perfect')),
)


class CommentForm(forms.ModelForm):
    score = forms.ChoiceField(widget=forms.RadioSelect, choices=SCORE_CHOICE)

    class Meta:
        model = Comment
        fields = ["massage", "score"]
        widgets = {
            "massage": forms.Textarea(attrs={"placeholder": _("Hello My Name IS...")}),
        }
        labels = {
            "massage": _("Message"),
            "score": _("Score"),
        }
