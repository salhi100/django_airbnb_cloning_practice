from django.contrib import admin
from django.utils.html import mark_safe  # marking safe for inputted scripts to Django
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


# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.inlines
class PhotoInline(admin.TabularInline):

    model = models.Photo


# admin panel url http://127.0.0.1:8000/admin/rooms/room/
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        # Charfield in ./models.py
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
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

    # raw_id_fields for selecting foreignkey/ManytoMany objects
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields
    raw_id_fields = ("host",)

    # Search field to find rooms
    # refer to search fields at https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
    search_fields = (
        "=city",
        # host is defined in ./models.py, username is defined in AbstractUser, in class User, in /users/models.py,
        # refer to lookup fields at https://docs.djangoproject.com/en/3.0/topics/db/queries/
        "^host__username",
    )

    # room information registering process gets easier
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal
    # many to many filter
    filter_horizontal = ("amenities", "facilities", "house_rules")

    # ordering rules
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.ordering
    # ordering = "price"

    # controlling admin
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-methods
    # def save_model(self, request, obj, form, change):
    #     print the html: object, did it change?, form
    #     print(obj, change, form)
    #     super().save_model(request, obj, form, change)

    # counting number of amenities
    # self is admin class, object is the room
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

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        # file object is not string, but class
        # print(type(obj.file))

        # you can look at stuffs that you can deal with the file
        # print(dir(obj.file))
        # return obj.file.url

        # returning html code (which is going to work as input) for the image url
        # return f'<img src="{obj.file.url}" />'  # format image source object file url
        # but it doesn't work for the sake of security. Django doesn't run all inputed scripts

        return mark_safe(f'<img width="300px" src="{obj.file.url}"')

    get_thumbnail.short_description = "Thumbnail"

    pass
