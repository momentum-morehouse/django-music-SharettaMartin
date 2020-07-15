from django.db import models

# Create your models here.
class Album(models.Model):

  artistname = models.CharField(max_length=255)
  albumtitle = models.CharField(max_length=255)
  releasedate = models.CharField(max_length=255)
#These are the 3 things display about the albums

def __str__(self):
      return f"{self.title} by {self.artist}"

class Users(models.Model):
  pass
  
  