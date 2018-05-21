from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('', include('music.urls')),
]
