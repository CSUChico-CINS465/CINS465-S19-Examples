from django import forms
# from django.core.validators import validate_slug

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppercase")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(label='Suggestion', max_length=240)
