# CMD click for BaseCommand Details
# class BaseCommand is at /Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py
import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_random_queryset import RandomManager

# Third Party app django seed docs: https://github.com/brobin/django-seed
# For faker library for django seed ap: https://faker.readthedocs.io/en/master/fakerclass.html
from django_seed import Seed

# my application
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"

# YOU CAN'T RUN IT TWICE, SINCE ROOMS ARE DESIGNATED WITH ONE UNIQUE USER: ONETOONE FIELD
# check seeded results here: http://127.0.0.1:8000/admin/reviews/review/
class Command(BaseCommand):

    help = f"This command creates fake {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"how many fake {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        # print(args, options)

        # get number from console
        number = options.get("number")
        seeder = Seed.seeder()

        # importing foreignkey field at models.py
        all_users = user_models.User.objects.all()
        all_rooms = room_models.Room.objects.all()
        print(all_users)

        # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#when-querysets-are-evaluated
        # users_list = list(all_users)
        # print(users_list)

        # add entities to seeder packet
        seeder.add_entity(
            list_models.List,
            number,
            # foreignkey field wrapped as queryset
            {"user": lambda x: random.choice(all_users)},
        )

        # inject seeder packet to the databse

        # executing seeder
        created = seeder.execute()

        # allocating random rooms to list
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            # getting list class item with primary key
            list_model = list_models.List.objects.get(pk=pk)
            # list of rooms from random number to random number
            random_int1 = random.randint(0, 5)
            random_int2 = random.randint(6, 30)
            to_add = all_rooms[random_int1:random_int2]
            # below is "rooms" field at lists.models class List
            list_model.rooms.add(*to_add)

        # stand out
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))
