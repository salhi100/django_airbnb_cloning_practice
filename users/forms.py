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


# using ModelForm to reduce repetetive scripting for fields
# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#modelform
class SignUpForm(forms.ModelForm):
    class Meta:
        # fetch model from User app
        model = models.User
        # INPUT FIELDS FOR THE USERS TO PUT IN WHEN SIGNUP
        fields = ("first_name", "last_name", "email", "birthdate")

    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    # cleaning password_again(field for confirmation)
    def clean_password_again(self):
        # get cleaned data from template
        password = self.cleaned_data.get("password")
        password_again = self.cleaned_data.get("password_again")
        # if fetched password doesn't match password again then raise validation error.
        if password != password_again:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            # return password to database
            return password

    # ModelForm has save method: https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method
    def save(self, *args, **kwargs):
        # Additional interception is taken place with commit=False: create object but don't put it in database
        user = super().save(commit=False)
        # email and password from the form
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        # username field of user app
        user.username = email
        # hashing password with set_password: https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        user.set_password(password)
        user.save()

    """
    # providing form fields to views.py -> urls.py -> template
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    


    # clean email data from user, received through template
    # ModelForm cleans email, so this part is not scripted
    def clean_email(self):
        # get cleaned data from template
        email = self.cleaned_data.get("email")
        # if finds existing user in database, then raise error
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists")
        # else, if it doesn't finds user in database, proceed sign up
        except models.User.DoesNotExist:
            # return email to database
            return email

    # registering user to the database
    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        # registering encrypted information to database
        user = models.User.objects.create_user(
            username=email, email=email, password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        user.save()


    """

