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

    # making table-like display on admin page
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

    list_filter = ("instant_book", "city")

    # refer to search fields at https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
    # ^	-> startswith, = -> iexact, @ -> search, None(default) -> icontains
    search_fields = ("=city", "^host__username")

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass
