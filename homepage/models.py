from django.db import models
from django.conf import settings
from django.urls import reverse

class Post(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     nickname = models.CharField(max_length=100, verbose_name="닉네임")
     tags = models.CharField(max_length=50, blank=True)
     content = models.TextField(verbose_name="설명")
     cat = models.CharField(max_length=100, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


