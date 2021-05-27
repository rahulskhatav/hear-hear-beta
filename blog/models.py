from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BArticle(models.Model):
    title = models.CharField(max_length=100, blank=False)
    caption = models.CharField(max_length=100, default="Wanna read more?", blank=False)
    date_posted = models.DateField(default=timezone.now)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)