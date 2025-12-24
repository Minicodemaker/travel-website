from django.utils import timezone
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Contact_table(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    desc=models.TextField(max_length=100)
    date=models.DateTimeField()

    def __str__(self):
        return self.name
        

class Destination(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)
    price=models.IntegerField()
    img=models.ImageField(upload_to='images/')
    time=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(unique=True,blank=True,null=True)
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)