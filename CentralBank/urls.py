from django.contrib import admin
from django.urls import path
# from django.conf.urls import url, include
from django.urls import include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name = "home"),
    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^profile/', include("profiles.urls")),
    re_path(r'^admins/', include("admins.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Change Site Title, Index Title and Site Title
admin.site.site_header = "Clarivate Bank Admin"
admin.site.site_title = "Clarivate Bank Admin"
admin.site.index_title = "Welcome to Clarivate Bank Admin Panel"
