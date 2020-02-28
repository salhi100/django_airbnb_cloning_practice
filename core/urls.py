from django.urls import path
from rooms import views as room_views

app_name = "core"

# core app's urls.py serves as globalRouter.js
# patterns of requested urls
# urlpatterns receives 1) urls (like "" or "/home") and 2) function
# Class HomeView has method as_view()
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
