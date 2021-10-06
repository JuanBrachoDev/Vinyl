from django import forms
from .widgets import CustomClearableFileInput
from .models import Album, Artist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'

    def clean(self):
        special_offer_category = self.cleaned_data.get('special_offer_category')
        print(special_offer_category)
        if special_offer_category != 'no_offer':
            # validate the activity name
            special_offer_price = self.cleaned_data.get('special_offer_price', None)
            print(special_offer_price)
            if special_offer_price is None:
                self._errors['special_offer_price'] = self.error_class([
                    'Special offer price required while offer is selected.'])
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
