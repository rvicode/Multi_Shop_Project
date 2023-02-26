from django import forms


class ProductCartForm(forms.Form):
    QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE, coerce=int)

    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
