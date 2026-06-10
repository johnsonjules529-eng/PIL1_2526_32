from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'etablissement',
            'filiere',
            'niveau_etude',
            'password1',
            'password2',
        )

class ProfilForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "etablissement",
            "filiere",
            "niveau_etude",
            "matieres",
            "competences",
            "centres_interet",
        ]

        widgets = {
            "matieres": forms.CheckboxSelectMultiple(),
            "competences": forms.CheckboxSelectMultiple(),
            "centres_interet": forms.CheckboxSelectMultiple(),
        }        