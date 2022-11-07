# from django.conf.urls import url
from django.urls import include, re_path
from . import views

app_name = "profiles"

urlpatterns = [
    re_path(r"^account_status/$", views.index, name = "account_status"),
    re_path(r"^money_transfer/", views.money_transfer, name = "money_transfer"),
    re_path(r"^loan_app/$", views.loan, name = "loan_app"),
    re_path(r"^ewallet/$", views.ewallet, name = "ewallet"),
    re_path(r"^online_pay/$", views.online_pay, name = "online_pay"),
    re_path(r"settings/$", views.settings, name = "settings"),
    re_path(r"edit_details/", views.edit_details, name = "edit_details"),
    # re_path(r"delete_account/$", views.delete_account, name = "delete_account")
]
