from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":20}))
