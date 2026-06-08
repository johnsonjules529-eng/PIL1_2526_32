# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('mentor', 'Mentor'),
        ('etudiant', 'Étudiant'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='etudiant'
    )

    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"