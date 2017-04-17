from django import forms

class Contactform(forms.Form):
    contact_name = forms.CharField(required=True, help_text="Ninjas have no name!")
    contact_email = forms.EmailField(required=True, help_text="example@example.com")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        help_text='I would love to hear from u!'
    )
