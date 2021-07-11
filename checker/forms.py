from django import forms

class UrlsForm(forms.Form):
    urls =  forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'placeholder': 'Cписок урлов через запятую', 'id':'urls'}))