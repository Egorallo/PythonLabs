from django import forms

SERVICEPACK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddServicePackForm(forms.Form):
    quantity = forms.TypedChoiceField(required=True, choices=SERVICEPACK_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=True, initial=False, widget=forms.HiddenInput)
    # quantity = forms.IntegerField(required=True)
    # update = forms.BooleanField(required=True)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be greater than or equal to 1")
        return quantity