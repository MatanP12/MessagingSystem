from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='receiver')
    subject = models.CharField(max_length = 200)
    message = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    is_readed = models.BooleanField(default = False)
    

