from django.db import models

# Create your models here.

restrict = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Male & Female", "Male & Female")
)

class Categorie(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
class Venue(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    catrgorie = models.ForeignKey(Categorie, on_delete = models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete = models.CASCADE, null = True)
    startTime = models.TimeField(blank=False)
    endTime = models.TimeField(blank=False)
    startDate = models.DateField(blank=False)
    endDate = models.DateField(blank=False)
    participation = models.CharField(max_length=20, choices = restrict, default = 'Both')
    approval = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

