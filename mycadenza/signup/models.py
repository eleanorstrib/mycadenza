from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CadenzaUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    mobile = PhoneNumberField()
    tracker_name = models.CharField(
                                    max_length=50,
                                    blank=True
                                    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username', 'mobile']
