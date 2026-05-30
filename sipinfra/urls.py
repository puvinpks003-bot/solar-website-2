from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.get_admin_site() if hasattr(admin, 'get_admin_site') else admin.site.urls),
    path('', include('solar_web.urls')),
]