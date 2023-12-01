from django.shortcuts import render
from app import forms
# Create your views here.
def front_times(request):
    form = forms.front_times_forms(request.GET)
    if form.is_valid():
        num = form.cleaned_data["num"]
        words = form.cleaned_data["words"]
        result = num * words[:3]
        return render(request, "front_times.html", {"forms": form, "result": result})
    else:
      return render(request, "front_times.html")
  
def no_teen_sum(request):
  form = forms.no_teen_sum_forms(request.GET)
  if form.is_valid():
     a = form.cleaned_data["a"]
     b = form.cleaned_data["b"]
     c = form.cleaned_data["c"]
     result = fix_teen(a) + fix_teen(b) + fix_teen(c)
     return render(request, "no_teen_sum.html",  {"forms": form, "result": result})
  else:
      return render(request,"no_teen_sum.html")
      
def fix_teen(n):
  teen = [13, 14, 17, 18, 19]
  if n in teen:
    return 0
  else:
    return n

def xyz_theres(request):
  form = forms.XYZ_theres_forms(request.GET)
  if form.is_valid():
     xyz = form.cleaned_data["xyz"]
     if xyz.count('xyz') > xyz.count('.xyz'):
      i = True
     else:
      i = False
     return render(request, "xyz_theres.html",  {"i" : i, "forms": form})
  else:
    return render(request,"xyz_theres.html") 

def centered_average(request):
  form = forms.center_average_forms(request.GET)
  if form.is_valid():
    my_list = []
    nums1 = form.cleaned_data["nums1"]
    nums2 = form.cleaned_data["nums2"]
    nums3 = form.cleaned_data["nums3"]
   
    my_list.append(nums1)
    my_list.append(nums2)
    my_list.append(nums3)
    trim = sorted(my_list)[1:-1]
    i= sum(trim) / len(trim)
    return render(request, "centered_average.html",  {"i": i, "nums1" : nums1,"nums2" : nums2, "nums3" : nums3, "forms": form})
  else:
    return render(request,"centered_average.html")

 

