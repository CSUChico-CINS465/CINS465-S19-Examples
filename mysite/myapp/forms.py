from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django.core.validators import validate_slug

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppercase")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(label='Suggestion', max_length=240)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
