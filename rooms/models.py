# first django
from django.db import models

# second third party apps
from django_countries.fields import CountryField

# third my applications
from core import (
    models as core_models,
)  # core_models are preventing repetition. Refer to #4.0 Lecture
from users import models as user_models

# Create your models here.
# Cloning Sample page: https://www.airbnb.com/rooms/22320269?location=Seoul&source_impression_id=p3_1581697502_PpMPhvPC73I2KD%2BU


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    # requiring room name, unlike users
    # Below are different types of fields that we can utilize
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    # importing foreignkey
    # foreign key is connecting one model to the other. source of the connection is room.
    # Foreignkey enables many to one relationship. For example, many instagram posts per user or many youtube posts per google user.
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    pass
