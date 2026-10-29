import uuid #built module used to generate universally unique identifiers
# its a 128-bit identifier designed to be unique across different records and systems

from django.db import models


class UUIDModel(models.Model):
    """Abstract base: a random UUID primary key instead of 1, 2, 3..."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    """Abstract base: records when a row was created and last changed."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True