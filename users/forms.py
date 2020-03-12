from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # get the email data that user sent to us, clean data
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        # try to find matching email object in Users database
        try:
            user = models.User.objects.get(email=email)
            # check_password(): https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.check_password
            # check_password() is encrypting password, and if the encrypted password is saved on the database
            if user.check_password(password):
                # always return cleaned data
                return self.cleaned_data
            else:
                # adding error on password field with error form
                self.add_error("password", forms.ValidationError("Wrong Password"))

        # if user's email object does not exist in db, add error
        # adding error on email field which prevents reaching to views.py LoginView Post request
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User Does Not Exists"))
