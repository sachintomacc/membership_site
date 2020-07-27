from django import forms
from .models import MembershipDetail, Donation


PAYMENT_MODE_CHOICES = (
    ('O', 'One Time'),
    ('M', 'Monthly'),
)


class DonationForm(forms.ModelForm):
    payment_mode = forms.ChoiceField(
        choices=PAYMENT_MODE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Donation
        fields = "__all__"


class MembershipDetailForm(forms.ModelForm):

    first_name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'disabled': True}))
    last_name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'disabled': True}))

    class Meta:
        model = MembershipDetail
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
