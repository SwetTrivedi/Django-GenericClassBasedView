from django import forms 

class Contactform(forms.Form):
    name=forms.CharField(max_length=70)
    email=forms.EmailField(max_length=70)
    msg=forms.CharField(widget=forms.Textarea)