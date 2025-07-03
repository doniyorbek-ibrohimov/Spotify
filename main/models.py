from django.db import models

class Singer(models.Model):
    name=models.CharField(max_length=50)
    birthdate=models.DateField()
    country=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField(upload_to='images/')
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.singer}-{self.name}"

class Song(models.Model):
    name=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    duration=models.DurationField()
    file=models.FileField()
    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.duration}"


