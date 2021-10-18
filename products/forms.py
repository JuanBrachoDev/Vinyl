from django import forms
from .widgets import CustomClearableFileInput
from .models import Album, Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

    def clean(self):
        special_offer_category = self.cleaned_data.get("special_offer_category")
        special_offer_price = self.cleaned_data.get("special_offer_price")
        price = self.cleaned_data.get("price")
        rating = self.cleaned_data.get("rating")

        # Validate price isn't zero or negative
        if price and price <= 0:
            self._errors["price"] = self.error_class(
                ["Price can't be a negative number."]
            )
        # Validate rating is a number between 1 and 5
        if rating and rating < 1 or rating and rating > 5:
            self._errors["rating"] = self.error_class(
                ["Rating must be a number between 1 and 5 (including both numbers)."]
            )
        # Validate special offer price is not None while a special offer category is selected
        if special_offer_category == "deal" or special_offer_category == "clearance":
            if special_offer_price is None:
                self._errors["special_offer_price"] = self.error_class(
                    [
                        "Valid special offer price required while offer is selected. "
                        "Special offer price can't be a negative number or zero, and it has to be lower than the original price."
                    ]
                )
        if special_offer_price is not None:
            # Validate special offer price is a valid price and lower than the original price
            if special_offer_price >= price or special_offer_price <= 0:
                self._errors["special_offer_price"] = self.error_class(
                    [
                        "Special offer price can't be a negative number or zero and it has to be lower than the original price."
                    ]
                )
            # Validate special offer category is selected while special offer price is entered
            if (
                special_offer_category == "no_offer"
                or special_offer_category == "new_arrival"
            ):
                self._errors["special_offer_category"] = self.error_class(
                    [
                        'Special offer "Deal" or "Clearance" categories required when a special offer price is entered.'
                    ]
                )
        return self.cleaned_data

    # Use custom image input
    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Field styling
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

    # Use custom image input
    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Field styling
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
