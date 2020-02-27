from django.urls import path
from rooms import views as room_views

app_name = "core"

# core app's urls.py serves as globalRouter.js
# patterns of requested urls
urlpatterns = [path("", room_views.all_rooms, name="home")]
