from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField #import this



# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=100,unique=True)
    url=models.SlugField(max_length=100,unique=True)
    def __str__(self):
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
    body=RichTextUploadingField()
    description=models.CharField(max_length=200)
    tags=TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to="static/images",blank=True)
    facebook=models.CharField(max_length=1000,default='#')
    twitter=models.CharField(max_length=1000,default='#')
    instagram=models.CharField(max_length=1000,default='#')
    quotes=models.TextField(blank=True)
    date=models.DateTimeField(default=timezone.now)
    staff=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    is_parent=models.BooleanField(default=True)
    parent = models.ForeignKey('self',blank=True, on_delete=models.CASCADE,null=True, related_name='replies')
    def __str__(self):
        return self.comment
    
