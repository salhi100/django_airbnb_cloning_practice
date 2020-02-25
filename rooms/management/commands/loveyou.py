# CMD click for BaseCommand Details
# class BaseCommand is at /Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command is to tell myam that I love her"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="how many times do you want me to tell you that I love myam?",
        )

    def handle(self, *args, **options):
        # print(args, options)
        times = options.get("times")
        for time in range(0, int(times)):
            # print("I love you myam")
            self.stdout.write(self.style.SUCCESS("I love myam"))

    print("hello")
