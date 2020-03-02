# first django
from django.db import models

# takes the name of url and returns the actual url
from django.urls import reverse

# second third party apps
from django_countries.fields import CountryField

# third my applications
from core import (
    models as core_models,
)  # core_models are preventing repetition. Refer to #4.0 Lecture

# from users import models as user_models

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
    # image field for storing image
    file = models.ImageField(upload_to="room_photos")  # saving pictures to room_photos

    # connecting with the Room. But Room is not defined, thus has to be done as string.
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

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
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )

    # many to many relationship
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    # when class is called, it is called as name
    def __str__(self):
        return self.name

    # intercepting changes made by admin panel
    # https://docs.djangoproject.com/en/3.0/ref/models/instances/#customizing-model-loading
    def save(self, *args, **kwargs):
        # print(self.city)
        self.city = str.capitalize(self.city)
        # call the real save() method from Django
        super().save(*args, **kwargs)

    # method of returning absolute url for the model
    def get_absolute_url(self):
        # <name of namespace in config urls.py> : <name of url patterns in rooms urls.py>
        # keworded arguments = {<url patterns path in rooms urls.py>: self.<url patterns path in rooms urls.py>}
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    # creating all reviews ratings average for a certain room
    def total_rating(self):
        # accessing queryset
        all_reviews = self.reviews.all()
        # print(all_reviews)
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                # print(review) # accessing objects inside of query set
                # print(review.rating_average())
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    pass
