from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
# This is admin panel for users. Refer to https://docs.djangoproject.com/en/2.2/ref/contrib/admin/


# @admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custum User Admin"""

    # refer to ./models.py for available options
    # list_display is in description of https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "currency", "language")

    # This is to make custom filter(or fieldsets) in Django admin panel.
    # UserAdmin.fieldsets: default fieldsets provided in Django. CMD + Click to check more information
    # Tuple added to UserAdmin.fieldsets are my customization
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    pass


# same as @admin.register(models.User) above
admin.site.register(models.User, CustomUserAdmin)
