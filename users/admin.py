from django.contrib import admin
from . import models

# Register your models here.
# This is admin panel for users. Refer to https://docs.djangoproject.com/en/2.2/ref/contrib/admin/


# @admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custum User Admin"""

    # refer to ./models.py for available options
    # list_display is in description of https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "currency", "language")
    pass


# same as @admin.register(models.User) above
admin.site.register(models.User, CustomUserAdmin)
