from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=512, blank=True)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

    def author(self):
        return f"{self.user.username}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
