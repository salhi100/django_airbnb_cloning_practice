# CMD click for BaseCommand Details
# class BaseCommand is at /Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py
import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

# Third Party app django seed docs: https://github.com/brobin/django-seed
# For faker library for django seed ap: https://faker.readthedocs.io/en/master/fakerclass.html
from django_seed import Seed

# my application
from rooms import models as room_models
from users import models as user_models


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

        # get all user objects
        # you should not do this in real life! We only have 50 users
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        print(room_types, all_users)

        # seed rooms entities to database
        # random choice within all_users or room_types
        # random integer between 0 and 5
        # using faker
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.text(),
                "address": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 5),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
            },
        )

        # executing seeder
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        # photo of id created
        print(created_clean)

        for pk in created_clean:
            # find room with primary key
            room = room_models.Room.objects.get(pk=pk)
            print(room)
            # create 3 ~ 14 rooms
            for i in range(random.randint(3, 14)):
                # creating photo
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )

        # stand out
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))

