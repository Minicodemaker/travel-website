from django.db import models
from django.utils.text import slugify

class Hotel_table(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='images/')
    desc=models.CharField(max_length=200)
    price=models.IntegerField()
    city=models.CharField(max_length=20)
    slug=models.SlugField(unique=True,blank=True,null=True)
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city)
        super().save(*args, **kwargs)


class Activity_table(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='images/')
    desc=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,blank=True,null=True)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
