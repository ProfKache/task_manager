import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from faker import Faker

from tasks.models import Task

User = get_user_model()


class Command(BaseCommand):
    """
    Insert random Tasks.
    """

    help = "Seed the database with fake task data"

    def handle(self, *args, **kwargs):
        faker = Faker()
        user = get_object_or_404(User, username="developer")
        users = list(User.objects.exclude(id=user.id))

        for _ in range(50):
            task = Task.objects.create(
                title=faker.text(),
                description=faker.text(),
                status=random.choice([choice[0] for choice in Task.StatusChoices.choices]),
                creator=user,
                owner=random.choice(users),
            )

            self.stdout.write(self.style.SUCCESS(f"Created task: {task.title}"))
