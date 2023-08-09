from django import forms

class NewOfferForm(forms.Form):
    
    CATEGORIES = (
        (1, 'Electronics'),
        (2, 'Fashion'),
        (3, 'Sport'),
        (4, 'Automobile'),
    )

    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput)
    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.RadioSelect)