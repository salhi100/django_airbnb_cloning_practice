from django.views import View
from django.shortcuts import render, redirect, reverse
from . import forms

# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authenticating-users
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    """ Login View """

    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        # print(form)

        # print(form.is_valid())
        if form.is_valid():
            # cleaned data is the cleaned result of all fields
            # print(form.cleaned_data)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


# https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-out
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
