from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=False)
    contact_email = forms.EmailField(required=False)
    content = forms.CharField(
        required=False,
        widget=forms.Textarea
    )