from django.db import models

# Create your models here.

# This is to skip repeating calling Django model.
# This will be used in all the other apps, except for Users app.
# Because User app already uses AbstractUser as model.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # prevents saving time stamp model on database
    class Meta:
        abstract = True
