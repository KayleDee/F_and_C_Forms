
from django.contrib import admin
from django.urls import path
from app.views import front_times, no_teen_sum, xyz_theres, centered_average
urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-2/front_times/",front_times, name="front_times" ),
    path("logic-2/no-teen-sum/", no_teen_sum, name="no_teen_sum"),
    path("string-2/xyz-there/", xyz_theres, name="xyz_theres"),
    path("list-2/centered-average/", centered_average,  name="centered_average")

]
