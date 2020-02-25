"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# django will know which settings.py that you've set up in project folder
from django.conf import settings
from django.conf.urls.static import static

# refer to settings.py
urlpatterns = [path("admin/", admin.site.urls)]

# When I am developping, I set DEBUG in settings.py as True
# When I am on production level (when server is live), I set DEBUG in settings.py False
# If I am developping, serve the files from the project folder
# If you are on production level, never put images on project server folder
if settings.DEBUG:
    # static connecting url with the folder
    # folder is media root
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
