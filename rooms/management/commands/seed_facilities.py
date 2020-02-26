# CMD click for BaseCommand Details
# class BaseCommand is at /Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py
from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        # print(args, options)
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for current_item in facilities:
            room_models.Facility.objects.create(name=current_item)
        # stand out
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created"))

