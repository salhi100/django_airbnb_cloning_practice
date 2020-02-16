from django.contrib import admin
from . import models  # from the same folder, import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    pass
