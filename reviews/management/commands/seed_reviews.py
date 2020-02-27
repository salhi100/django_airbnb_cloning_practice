# CMD click for BaseCommand Details
# class BaseCommand is at /Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py
import random
from django.core.management.base import BaseCommand

# Third Party app django seed docs: https://github.com/brobin/django-seed
# For faker library for django seed ap: https://faker.readthedocs.io/en/master/fakerclass.html
from django_seed import Seed

# my application
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates fake Rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many fake Rooms do you want to create?",
        )

    def handle(self, *args, **options):
        # print(args, options)

        # get number from console
        number = options.get("number")
        seeder = Seed.seeder()

        # importing foreignkey field at models.py
        all_users = user_models.User.objects.all()
        all_rooms = room_models.Room.objects.all()

        # add entities to seeder packet
        seeder.add_entity(
            review_models.Review,
            number,
            {  # random integer between 1 ~ 5
                "cleanliness": lambda x: random.randint(0, 6),
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "accessibility": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                # foreignkey field
                "room": lambda x: random.choice(all_rooms),
                "user": lambda x: random.choice(all_users),
            },
        )

        # inject seeder packet to the databse
        seeder.execute()

        # stand out
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created"))

