from django.urls import include, path
from django.conf import settings

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # It's a convention to match the trailing / as well
    path('matboje/', include('matboje.urls')),
]
