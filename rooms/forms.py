# django app
from django import forms

# my python files
from . import models

# thirdparty app
from django_countries.fields import CountryField


# Making forms should be same as fieldsname as models.py
# https://docs.djangoproject.com/en/2.2/ref/forms/api/
# Field arguments such as default, required can be looked up here https://docs.djangoproject.com/en/2.2/ref/forms/fields/
class SearchForm(forms.Form):
    # Widget customization: https://docs.djangoproject.com/en/2.2/ref/forms/fields/#widget
    # can't add required=False nor default=False to Charfield. > if city != "Anywhere": to do not require the form field
    city = forms.CharField(initial="Anywhere", widget=forms.Textarea)
    country = CountryField(default="KR").formfield()
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)

    # foreignkey field should connect to models.py with queryset of the class
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any Kind", queryset=models.RoomType.objects.all()
    )
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    pass
