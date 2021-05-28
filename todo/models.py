from django.db import models
from django.utils import timezone

from norilog.models import CustomUser

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    # body = models.CharField(max_length=200, verbose_name='タスク')
    body = models.TextField(verbose_name='タスク')
    created_at = models.DateTimeField(default=timezone.now ,verbose_name='作成日')

    class Meta:
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'

    def __str__(self):
        return self.body