from django import forms
from .widgets import CustomClearableFileInput
from .models import Album, Artist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'

    def clean(self):
        special_offer_category = self.cleaned_data.get('special_offer_category')
        special_offer_price = self.cleaned_data.get('special_offer_price')
        if special_offer_category == 'deal' or special_offer_category == 'clearance':
            # validate the activity name
            if special_offer_price is None:
                self._errors['special_offer_price'] = self.error_class([
                    'Special offer price required while offer is selected.'])

        if special_offer_price is not None:
            # validate the activity name
            if special_offer_category == 'no_offer' or special_offer_category == 'new_arrival':
                self._errors['special_offer_category'] = self.error_class([
                    'Special offer "Deal" or "Clearance" categories required when a special offer price is entered.'])

        return self.cleaned_data

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
