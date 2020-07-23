from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_user_prefereces = models.BooleanField(default=False)
    option_1 = models.BooleanField(default=False)
    option_2 = models.BooleanField(default=False)
    option_3 = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

