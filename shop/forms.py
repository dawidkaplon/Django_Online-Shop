from django import forms
from .models import Category

# Fetching all categories from the database and converting them to a list of tuples
CATEGORIES= Category.objects.values_list('id', 'name')

class NewOfferForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput)
    category = forms.ChoiceField(choices=list(CATEGORIES), widget=forms.RadioSelect)
    image = forms.ImageField()


class EditOfferForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput)
    category = forms.ChoiceField(choices=list(CATEGORIES), widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        item = kwargs.pop("item", None)
        super(EditOfferForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['price'].required = False
        self.fields['category'].required = False
        

        if item:
            self.fields["name"].widget.attrs["placeholder"] = item.name
            self.fields["description"].widget.attrs["placeholder"] = item.description
            self.fields["price"].widget.attrs["placeholder"] = item.price 
