from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Django Model Reference: https://docs.djangoproject.com/en/2.2/ref/models/fields/


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
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    # boolean field is true of false
    superhost = models.BooleanField(default=False)
    pass
