from django.db import models

class Place(models.Model):
    img=models.ImageField(upload_to='travel/img',null=True,blank=True)
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Team(models.Model):
    img=models.ImageField(upload_to='travel/img',null=True,blank=True)
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)

    def __str__(self):
        return self.name


