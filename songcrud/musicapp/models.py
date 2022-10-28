from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name =models.CharField(max_lenght=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    
class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.CharField(max_length=50)
    likes = models.CharField(max_length=50)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.DO_NOTHING, related_name="artiste")
        
class Lyrics(models.Model):
    content = models.CharField(max_length=200)
    song_id =models.ForeignKey(Song, on_delete=DO_NOTHING,related_name="song")


