from django import forms

class MyForms(forms.Form):
    title = forms.CharField(label='title', max_length=300)
    content = forms.CharField(label='Content')
    enable = forms.BooleanField()
