from django import forms

class age_in_form(forms.Form):
    age = forms.IntegerField()
    year = forms.IntegerField()

class hey_you_form(forms.Form):
    user_name = forms.CharField()

class can_i_take_your_order(forms.Form):
    fries = forms.IntegerField()
    burger = forms.IntegerField()
    drink = forms.IntegerField()