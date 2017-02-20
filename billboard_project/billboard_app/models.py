from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100, null=True)
    message = models.CharField(max_length = 400, null=True)
    author = models.CharField(max_length = 50, null=True)
    pub_date = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    message= models.CharField(max_length=200, null=True)
    post_id = models.ForeignKey(Post)
