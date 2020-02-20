from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    # ./models.py has two functions of __str__ and rating_average
    list_display = (
        "__str__",
        "rating_average",
    )


pass
