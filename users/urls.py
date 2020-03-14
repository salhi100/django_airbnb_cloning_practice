from django.urls import path
from . import views

# exporting user's url routing to django project
app_name = "users"

# get functions from user app's views.py, export them to templates as name="name"
urlpatterns = [
    # importing Class based views from ./views.py
    path("login", views.LoginView.as_view(), name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    # importing function based views from ./views.py
    path("logout", views.log_out, name="logout"),
    path(
        "verify/<str:verification_key>",
        views.complete_verification,
        name="complete-verification",
    ),
]
