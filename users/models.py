"""User's models"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    """Profile model.
    We use proxy model that extends the base data with
    other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username