from django import forms

class front_times_forms(forms.Form):
    num = forms.IntegerField()
    words = forms.CharField()

class no_teen_sum_forms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()

class XYZ_theres_forms(forms.Form):
    xyz = forms.CharField() 

class center_average_forms(forms.Form):
    nums1 = forms.IntegerField()
    nums2 = forms.IntegerField()
    nums3 = forms.IntegerField()