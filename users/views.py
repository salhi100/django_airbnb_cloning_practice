from django.views import View
from django.shortcuts import render
from . import forms


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
            print(form.cleaned_data)
        return render(request, "users/login.html", {"form": form})

