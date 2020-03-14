# importing settings.py file of django project
from django.conf import settings

# Utilizing Django's AbstractUser class
from django.contrib.auth.models import AbstractUser
from django.db import models

# email verification
# send_mail function from django: https://docs.djangoproject.com/en/3.0/topics/email/#quick-example
from django.core.mail import send_mail

# strip html tags from string
from django.utils.html import strip_tags

# import html from templates folder, render it to use as string
from django.template.loader import render_to_string

# random secret key generator for email verification
import uuid

# Inheriting Django's AbstractUser Class and doing further customization
class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # null is for the database, and blank is for forms on website
    # null means "empty values are acceptable", and blank also means the same.
    avatar = models.ImageField(
        upload_to="avatars", blank=True
    )  # saving pictures to avatars folder

    # charfield: text field with limit of single line
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # Adding column(field) to database with empty

    # textfield: text field without limit
    bio = models.TextField(default="", blank=True)
    # bio = models.TextField(null=True) # Or, empty cell in field is accepted

    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_ENGLISH
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_USD
    )

    # boolean field is true of false
    superhost = models.BooleanField(default=False)

    # email fields added to models.py
    # emailing with django
    email_confirmed = models.BooleanField(default=False)
    # randomly generated numbers for email confirmation
    email_secret = models.CharField(max_length=20, default="", blank=True)

    # ------------------- end of the database fields -------------------------------

    # email verification method connected with ./views.py
    def verify_email(self):
        if self.email_confirmed is False:
            # using python random generator uuid library
            # result is form of tuple, needs to be indexed like list
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            # importing html message from static template, render it to string and use it to send_mail
            html_message = render_to_string(
                "emails/verify_email.html", context={"secret": secret}
            )
            # check django's send_email function's example https://docs.djangoproject.com/en/3.0/topics/email/#quick-example
            # for specific arguments for the function, refer here: https://docs.djangoproject.com/en/3.0/topics/email/#send-mail
            send_mail(
                # email title
                "Verify AirBnB Account",
                # email content without html tags
                strip_tags(html_message),
                # email sender setted up in settings.py as no-reply
                settings.EMAIL_FROM,
                # recipient_list
                [self.email],
                # not raising error even if it failed, or raise
                fail_silently=False,
                # html
                html_message=html_message,
            )
            return
