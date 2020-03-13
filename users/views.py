from django.views import View
from django.shortcuts import render, redirect, reverse

# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/FormView/
from django.views.generic import FormView

# reverse_lazy to prevent circular import
from django.urls import reverse_lazy

# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authenticating-users
from django.contrib.auth import authenticate, login, logout

# import users app's login forms
from . import forms


class LoginView(FormView):

    """ Login View """

    # Using inherited FormView class instead of LoginView: https://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/FormView/
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        # getting function from models.py users app, verify user by sending randomly genearated string
        user.verify_email()

        return super().form_valid(form)

    """
    # function based view for post request
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
    """


# Logout function: https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-out
# LogoutView class: https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LogoutView
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    # Using inherited FormView class: https://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/FormView/
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    # intially providing an example to users for signup
    initial = {
        "first_name": "Gildong",
        "last_name": "Hong",
        "email": "honggildong@gmail.com",
    }

    # to see where "form" came from, CMD + Click on FormView inherited class
    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

