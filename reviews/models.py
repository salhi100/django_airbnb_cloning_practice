from django.db import models
from core import models as core_models

# cloning reviews like https://www.airbnb.com/rooms/3993887?source_impression_id=p3_1581822726_vSiWIHiIREsnsKZW


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    content = models.TextField()  # empty the field to require the field
    cleanliness = models.IntegerField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    accessibility = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    # connecting review database with user tables
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )

    # pointing rooms tables with reviews database
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        # Thanks to foreignkey code line above, Django is accessing to room application and extracting data from there
        # return self.room.host

        # Django is accessing deeper. accessing room app, and then accessing user app.
        # return self.room.host.username

        return f"{self.content} - {self.room}"  # {} is filling up string with variable


# Create your models here.
