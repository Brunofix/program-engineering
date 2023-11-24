from django.db import models

# Create your models here.
class image(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=512, blank=True)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=512)

    def __str__(self) :
        return self.title