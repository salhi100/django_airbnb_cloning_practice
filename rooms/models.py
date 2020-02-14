from django.db import models

# core_models are preventing repetition. Refer to #4.0 Lecture
from core import models as core_models

# Create your models here.


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    # requiring room name, unlike users
    name = models.CharField(max_length=140)
    description = models.TextField()

    pass

