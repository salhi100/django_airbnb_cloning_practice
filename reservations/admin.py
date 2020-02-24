from django.contrib import admin
from . import models  # get functions from models.py

# http://127.0.0.1:8000/admin/reservations/reservation/
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition"""

    # showing tables on admin panel
    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    # showing in progress status

    list_filter = (
        "status",
        # "in_progress",
        # "is_finished",
    )

    pass
