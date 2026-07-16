from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        default="profiles/default.png"
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=20,
        choices=[
            ("Male","Male"),
            ("Female","Female"),
            ("Other","Other")
        ],
        blank=True
    )

    def __str__(self):
        return self.user.username