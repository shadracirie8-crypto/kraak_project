from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # On définit les constantes pour les rôles
    ADMIN = 'ADMIN'
    CLIENT = 'CLIENT'
    EMPLOYE = 'EMPLOYE'

    ROLE_CHOICES = (
        (ADMIN, 'Administrateur'),
        (CLIENT, 'Client'),
        (EMPLOYE, 'Employé'),
    )
    
    # On ajoute le champ role à l'utilisateur
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default=CLIENT
    )

    # Petites méthodes pratiques pour tester le rôle facilement
    def is_admin(self):
        return self.role == self.ADMIN

    def is_client(self):
        return self.role == self.CLIENT

    def is_employe(self):
        return self.role == self.EMPLOYE