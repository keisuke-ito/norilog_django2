from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Noriori(models.Model):
    class Meta:
        verbose_name = '乗降履歴'
        verbose_name_plural = '乗降履歴'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start = models.CharField(max_length=31)
    finish = models.CharField(max_length=31)
    memo = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created_at)
