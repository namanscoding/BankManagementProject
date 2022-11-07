# from django.conf.urls import url
from django.urls import include, re_path
from . import views

app_name = "accounts"

urlpatterns = [
    re_path(r"^register/$", views.register, name = "signup"),
    re_path(r"^login/$", views.sign_in, name = "signin"),
    re_path(r"^logout/$", views.logout_view, name = "logout"),
]
