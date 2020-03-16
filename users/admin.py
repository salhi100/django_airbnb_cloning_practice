from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
# This is admin panel for users. Refer to https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

# UserAdin is calling Django
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custum User Admin"""

    # This is to make custom filter(or fieldsets) in Django admin panel.
    # UserAdmin.fieldsets: default fieldsets provided in Django. CMD + Click to check more information.
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
                    "register_login_method",
                    "email_confirmed",
                )
            },
        ),
    )

    # right-hand sidebar of admin panel for filter
    list_filter = UserAdmin.list_filter + ("superhost", "currency", "language")

    # showing tables on admin panel
    # refer to ./models.py for available options
    # list_display is in description of https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
    list_display = (
        "username",
        "first_name",
        "last_name",
        "register_login_method",
        "email",
        "email_confirmed",
        "email_verification_key",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

    pass


# same as @admin.register(models.User) above
# admin.site.register(models.User, CustomUserAdmin)
