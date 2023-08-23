from django.db import models

# Create your models here.
class PLace(models.Model):
    name=models.CharField(max_length=255)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class Team(models.Model):
    member_name=models.CharField(max_length=255)
    prof_pic=models.ImageField(upload_to='Team')
    member_desc=models.TextField()

    def __str__(self):
        return self.member_name
