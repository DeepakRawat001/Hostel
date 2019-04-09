from django.db import models

class Movie(models.Model):
    actor=models.CharField(max_length=30)
    actor_movie=models.CharField(max_length=50)
    def  __str__ (self):
        return(self.actor)

class Song(models.Model):
    movie=models.ForeignKey(Movie , on_delete=models.CASCADE)
    file_type=models.CharField(max_length=100)
    #is_favourite=models.BooleanField(default=False)


    def __str__(self):
        return self.song_name

