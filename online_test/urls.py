from django.conf.urls import include, url
from django.contrib import admin

from web.views import HomePage

urlpatterns = [
    url(r'^settings_page/', include(admin.site.urls)),
    url(r'^', HomePage.as_view(), name="home"),
]
