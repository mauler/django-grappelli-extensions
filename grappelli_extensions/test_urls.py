from django.conf.urls import url, include, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
)
