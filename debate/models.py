from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.
class motion(models.Model):
    levels = (
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
        ('EX', 'Expert'),
    )
    title = models.CharField(max_length=500)
    context = models.TextField(blank=True)
    date_posted = models.DateField(default=timezone.now)
    difficulty = models.CharField(max_length=2, choices=levels)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # def save(self,*args, **kwargs):
    #     super(motion, self).save(*args, **kwargs)

class argument(models.Model):
    sides = (
        ('PROP', 'Proposition'),
        ('OPP', 'Opposition'),
    )
    side = models.CharField(max_length=4, choices=sides)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    to_motion = models.ForeignKey(motion, on_delete=models.CASCADE)

class subpoint(models.Model):
    sides = (
        ('PROP', 'Proposition'),
        ('OPP', 'Opposition'),
    )
    side = models.CharField(max_length=4, choices=sides)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    to_arg = models.ForeignKey(argument, on_delete=models.CASCADE)



