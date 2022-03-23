"""config URL Configurationtitle

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.shortcuts import redirect
# from pybo.views import base_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/insta/', permanent=True)),
    path('insta/', include('insta.urls')),

    # path('', include('insta.urls')),  # '/' 에 해당되는 path

    path('common/', include('common.urls')),


    # path('', lambda request: redirect('insta/')),

    # path('', include('photo.urls')),  # '/' 에 해당되는 path
    # path('', lambda request: redirect('photo/')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)