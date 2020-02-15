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

# Look at concept of inherities of many different classes below.


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Type"
        ordering = [
            "name"
        ]  # ordering https://docs.djangoproject.com/en/3.0/ref/models/options/

    pass


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    # verbose name stands for name that appears in admin webpage
    class Meta:
        verbose_name_plural = "Amenities"

    pass


class Facility(AbstractItem):
    """ Facility Model Definition"""

    # verbose name stands for name that appears in admin webpage
    class Meta:
        verbose_name_plural = "Facilities"

    pass


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    # verbose name stands for name that appears in admin webpage
    class Meta:
        verbose_name = "House Rule"

    pass


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()  # image field for storing image

    # connecting with the Room. But Room is not defined, thus has to be done as string.
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# Shaping Database(or table) of rooms
# All of classes above are inherited here.
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

    # importing foreignkey https://docs.djangoproject.com/en/3.0/ref/models/fields/
    # foreign key is connecting one model to the many other. source of the connection is user, and it connects to multiple rooms.
    # Foreignkey enables many to one relationship, not many to many. For example, many instagram posts per user or many youtube posts per google user.
    # on_delete cascade: when you delete the user, delete also the room
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)

    # many to many relationship
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    pass

