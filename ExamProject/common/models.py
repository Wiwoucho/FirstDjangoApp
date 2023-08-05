from django.db import models
from .validators import guests_validator
from django.contrib.auth.models import User


class TripBooking(models.Model):
    city = models.CharField(
        max_length=100,
        blank=False,
        null = False
    )
    guests = models.PositiveIntegerField(
        blank=False,
        null = False,
        validators = [guests_validator]
    )
    start_date = models.DateField()
    end_date = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)
