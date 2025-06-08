from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

User = get_user_model()


class Command(BaseCommand):
    """
    Insert random Tasks.
    """

    help = "Seed the database with sammple user data"

    def handle(self, *args, **kwargs):
        faker = Faker()
        for _ in range(20):
            User.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password=faker.password(),
            )
        self.stdout.write(self.style.SUCCESS("Created 20 users"))
