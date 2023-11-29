from django import forms

class age_in_form(forms.Form):
    age = forms.IntegerField()
    year = forms.IntegerField()

class hey_you_form(forms.Form):
    user_name = forms.CharField()