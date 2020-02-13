from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


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

    # null is for the database, and blank is for forms on website
    # null means "empty values are acceptable", and blank also means the same.
    avatar = models.ImageField(null=True, blank=True)
    # charfield: text field with limit of single line
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    # Adding column(field) to database with empty
    # textfield: text field without limit
    bio = models.TextField(default="")

    # Or, empty cell in field is accepted
    # bio = models.TextField(null=True)
    pass

