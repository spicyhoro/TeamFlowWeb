from django.db import models
from django.conf import settings
from django.forms import ValidationError
import re
from django.urls import reverse


def phone_number_validator(value):
     if not re.match(r'^\d{3}-\d{3,4}-\d{4}$/', value):
          raise ValidationError('Invalid Phone_number Type')


class Post(models.Model):
     STATUSE_CHOICES = (
          ('d', 'Draft'),
          ('p', 'published'),
     )





     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     nickname = models.CharField(max_length=100, verbose_name="닉네임",
                                 help_text="닉네임을 정해주세요")
     tags = models.CharField(max_length=50, blank=True,
                             help_text="나의 특징을 태그")
     content = models.TextField(verbose_name="설명",
                                help_text="나 한문장으로 적어주세요")
     phone_number =models.CharField(max_length=50, blank=True)
     cat = models.CharField(max_length=100, blank=True)
     status = models.CharField(max_length=1, choices=STATUSE_CHOICES)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.nickname

     class Meta:
          ordering = ['-id']



