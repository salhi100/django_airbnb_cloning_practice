from django.db import models
from django.utils import (
    timezone,
)  # timezone utility from django, which translates timezones of users
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    # Datefield
    check_in = models.DateField()
    check_out = models.DateField()

    # ForeignKey to access users table
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # For admin panel and also for the console
    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return (
            now > self.check_in and now < self.check_out
        )  # returning true or false value

    in_progress.boolean = True  # marking x on the in progress on admin panel

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

