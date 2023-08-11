from django.db import models
from django.core import validators
from django.contrib.auth.models import User



class AddBookingModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    price = models.PositiveIntegerField(
        null = False,
        blank = False,
        validators = [validators.MinValueValidator(1)]
    )
    name = models.CharField(
        max_length = 50,
        blank = False,
        null = False,
    )
    locations = models.CharField(
        blank = False,
        null = False,
        max_length = 50
    )
    guests = models.PositiveIntegerField(
        blank = False,
        null = False,
        validators = [validators.MinValueValidator(1)]
    )

class BookingImageModel(models.Model):
    booking = models.ForeignKey(AddBookingModel, on_delete=models.CASCADE, related_name = 'images')
    images = models.FileField(upload_to = 'user_pictures', blank = False, null = False)



class LoginModel(models.Model):
    username = models.CharField(
        max_length = 30,
        blank = False,
        null = False,
    )

    password = models.CharField(
        max_length = 30,
        blank = False,
        null = False,
    )