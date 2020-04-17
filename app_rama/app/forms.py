from django import forms


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(label="name@domain.co.uk")
    desc = forms.CharField()

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)