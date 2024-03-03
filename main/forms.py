from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Ismingiz', max_length=100)
    your_email = forms.EmailField(label='Email manzilingiz')