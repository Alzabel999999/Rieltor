from django import forms
from .models import Edit

class Write(forms.Form):
    price = forms.CharField(max_length=120, label='')
    about = forms.CharField(max_length=120, label='')
    coment = forms.CharField(label="", widget=forms.Textarea)
    image = forms.ImageField(label='')
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='')

    """class Meta:
        model = Edit
        fields = ('price', 'about', 'coment', 'image')"""

class User(forms.Form):
    username = forms.CharField(label='', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

