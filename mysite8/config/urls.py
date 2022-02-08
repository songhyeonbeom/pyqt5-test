
from django.contrib import admin
from django.urls import path, include
from photo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('photo/', include('photo.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)