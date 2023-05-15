from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=100,unique=True)
    url=models.SlugField(max_length=100,unique=True)
    def __str___(self):
        return self.name
class Newsletter(models.Model):
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.email

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    url=models.SlugField(max_length=1000,unique=True)
    title=models.CharField(max_length=1000)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/images')
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE,blank=True,related_name='categories')
    body=models.TextField()
    tags = TaggableManager() 
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
class Profile(User):
    desc=models.TextField(User,blank=True)
    image=models.ImageField(User,blank=True)
    quotes=models.TextField(User,blank=True,max_length=1000)