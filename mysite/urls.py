from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)