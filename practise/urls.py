from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path('two_factor/', include(('admin_two_factor.urls', 'admin_two_factor'), namespace='two_factor')),
    path('admin/', admin.site.urls),
    path('', include('main.urls'),),
    path('posts/', include('posts.urls')),
]

handler404 = 'main.views.custom_404_view'

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

