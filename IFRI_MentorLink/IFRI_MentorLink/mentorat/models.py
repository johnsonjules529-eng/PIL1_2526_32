# Create your models here.
from django.db import models
from accounts.models import User


class Mentorat(models.Model):
    mentor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mentorats_mentor'
    )

    etudiant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mentorats_etudiant'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.mentor.username} -> {self.etudiant.username}"