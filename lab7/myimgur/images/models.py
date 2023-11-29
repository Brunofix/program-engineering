from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=512, blank=True)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.title

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    content = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.content[:30]}"
