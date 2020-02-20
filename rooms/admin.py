from django.contrib import admin
from . import models  # from the same folder, import models


# refer ./models.py
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    # making admin panel for amenities: how many of amenities are used for registered rooms
    # http://127.0.0.1:8000/admin/rooms/amenity/
    def used_by(self, obj):
        return obj.rooms.count()

    pass


# admin panel url http://127.0.0.1:8000/admin/rooms/room/
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
    # many to many fields cannot be here
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
        "count_amenities",
        "count_photos",
        "total_rating",
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

    # ordering rules
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.ordering
    # ordering = "price"

    # counting number of amenities
    # self is admin class
    # object is the room
    def count_amenities(self, obj):
        # print(obj) #prints name of room object
        return obj.amenities.count()

    # renaming table at the admin panel
    count_amenities.short_description = "number of amenities"

    # counting number of photos registered to the room
    def count_photos(self, obj):
        return obj.photos.count()


# handling media files
# http://127.0.0.1:8000/admin/rooms/photo/
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass
