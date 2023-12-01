
from django.contrib import admin
from django.urls import path
from app.views import how_old, hey_you, your_order

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("age-in", how_old, name="age-in"),
    path("hey-you", hey_you, name="hey-you"),
    path("can_i_take_your_order", your_order, name="can_i_take_your_order")
]
