from django import forms

class UserPreferencesForm(forms.Form):
    option_1 = forms.BooleanField(required=False)
    option_2 = forms.BooleanField(required=False)
    option_3 = forms.BooleanField(required=False)
