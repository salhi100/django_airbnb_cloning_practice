# CMD click for BaseCommand Details
# class BaseCommand is at /Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py
from django.core.management.base import BaseCommand

# Third Party app django seed docs: https://github.com/brobin/django-seed
from django_seed import Seed

# my application
from users.models import User


class Command(BaseCommand):

    help = "This command creates fake users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many fake users do you want to create?",
        )

    def handle(self, *args, **options):
        # print(args, options)

        # get number from console
        number = options.get("number")
        seeder = Seed.seeder()

        # Inheritance of User class -> AbstractUser class. Field name 'is_staff"
        # Inheritance of User class -> AbstractUser class -> PermissionsMixin class. Field name "is_superuser"
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})

        # executing seeder
        seeder.execute()

        # stand out
        self.stdout.write(self.style.SUCCESS(f"{number} users created"))

