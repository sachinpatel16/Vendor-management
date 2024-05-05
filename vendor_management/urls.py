from django.contrib import admin
from django.urls import path,include

from vendor.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home,name="home"),
    path("api/",include('vendor.urls')),
]
