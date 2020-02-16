from django.db import models
from core import models as core_models

# refer to https://www.airbnb.com/s/Armenia/homes?_ga=2.92546461.1229078274.1581649756-1879266398.1581144278


class List(core_models.TimeStampedModel):
    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        "users.User", related_name="list", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
