from django.contrib import admin
from django.urls import path, include

# django will know which settings.py that you've set up in project folder
from django.conf import settings
from django.conf.urls.static import static


# patterns of requested urls
urlpatterns = [
    # dividing router to core app's urls.py
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]

# When I am developping, I set DEBUG in settings.py as True
# When I am on production level (when server is live), I set DEBUG in settings.py False
# If I am developping, serve the files from the project folder
# If you are on production level, never put images on project server folder
if settings.DEBUG:
    # static connecting url with the folder
    # folder is media root
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
