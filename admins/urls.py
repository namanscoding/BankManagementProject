# from django.conf.urls import url
from django.urls import include, re_path
from . import views

app_name = "admins"

urlpatterns = [
    re_path(r"^$", views.index, name = "admin_index"),
]
