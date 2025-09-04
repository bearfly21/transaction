import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
class CustomUser(AbstractUser):
    username = None
    email = models.CharField(unique=True)
    is_email_confirmed = models.BooleanField(default=False)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    
class Token(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(CustomUser, related_name="user_tokens", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)







