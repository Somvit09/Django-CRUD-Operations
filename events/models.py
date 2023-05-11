from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=150)
    tagline = models.CharField(max_length=250)
    schedule = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=250)
    files = models.ImageField(upload_to=('events/images/'), blank=True, null=True)
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    rigor_rank = models.IntegerField()
    attendees = models.ManyToManyField(User, related_name='events_attending')

    def __str__(self) -> str:
        return self.name

