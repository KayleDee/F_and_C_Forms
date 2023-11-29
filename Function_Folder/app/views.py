from django.shortcuts import render
from app import forms

# Create your views here.
def how_old(request):
    form = forms.age_in_form(request.GET)
    if form.is_valid():
        user_age = form.cleaned_data["age"]
        desired_year = form.cleaned_data["year"]
        total = desired_year - user_age

        return render(request, "age.html", {"A": user_age, "B": desired_year, "total": total})
    else:
        return render(request, "age.html")
    
def hey_you(request):
    form = forms.hey_you_form(request.GET)
    if  form.is_valid():
        user_name = form.cleaned_data["user_name"]

        return render(request, "hey.html", {"A": user_name})
    else:
        return render(request, "hey.html")