from django.conf import settings
from django.db import models


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        UNASSIGNED = "UNASSIGNED", "Unassigned"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Completed"
        ARCHIVED = "ARCHIVED", "Archived"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.UNASSIGNED,
        db_comment="Can be UNASSIGNED, IN_PROGRESS, DONE or ARCHIVED",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="created_tasks", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="owned_tasks",
        on_delete=models.SET_NULL,
        null=True,
        db_comment="Foreign Key to the user who currently owns the task.",
    )

    class Meta:
        db_table_comment = "Holds information about the tasks"
