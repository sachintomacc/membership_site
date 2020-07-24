from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Preference(models.Model):
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.option



class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    saved_user_prefereces = models.BooleanField(default=False)
    preferences = models.ManyToManyField(Preference)

    def __str__(self):
        return self.user.username
