from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'message'}), max_length=1000, required=True)