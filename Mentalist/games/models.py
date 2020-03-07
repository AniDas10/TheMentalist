from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    result = models.IntegerField(null=True, default=None)
    result_percent = models.DecimalField(max_digits=4, decimal_places=2, null=True, default=None)

class UserMetaData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disorder = models.CharField(max_length=32, null=True, default=None)
    current_session = models.ForeignKey(Session, on_delete=models.SET_NULL, default=None, null=True)

class Game(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    score = models.IntegerField()
    question = models.TextField()
    answer = models.TextField(null=True, default=None)