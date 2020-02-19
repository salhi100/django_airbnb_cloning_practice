from django.contrib import admin
from . import models  # from the same folder, import models

# refer ./models.py
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        # Charfield in ./models.py
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        # Timefield in ./models.py
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        # Integerfield in ./models.py
        ("Spaces", {"fields": ("guests", "beds", "bedrooms")}),
        # ManytoManyField in ./models.py
        ("More About the Space", {"fields": ("facilities", "amenities",)}),
        ("Last Details", {"fields": ("host",)}),
    )

    # making table-like display on room admin page
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "room_type",
    )

    # making filter on the right side of room admin page
    list_filter = (
        "instant_book",
        "room_type",
        "city",
        "facilities",
        "amenities",
        # host is defined in ./models.py
        "host__superhost",
    )

    # Search field to find rooms
    # refer to search fields at https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
    # ^	-> startswith, = -> iexact, @ -> search, None(default) -> icontains
    # host is defined in ./models.py
    # username is defined in AbstractUser, in class User, in /users/models.py,
    # refer to lookup fields at https://docs.djangoproject.com/en/3.0/topics/db/queries/
    search_fields = (
        "=city",
        "^host__username",
    )

    # room information registering process gets easier
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal
    # many to many filter
    filter_horizontal = ("amenities", "facilities", "house_rules")
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass
