from django.contrib import admin
from . import models  # from the same folder, import models

# http://127.0.0.1:8000/admin/lists/list/
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    list_display = ("name", "user", "count_rooms")

    # list_filter = ("status",)

    # search by on admin page
    search_fields = ("name",)

    # adding rooms to the list by search and select on admin panel
    filter_horizontal = ("rooms",)
    pass
