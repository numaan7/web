from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from blog.models import Categorie
from ckeditor_uploader.fields import RichTextUploadingField #import this

# Create your models here.


class Seller(models.Model):
    name=models.CharField(max_length=100,unique=True)
    url=models.SlugField(max_length=100,unique=True)
    description=RichTextUploadingField(default='this is seller description')
    def __str___(self):
        return self.name
    
class Offer(models.Model):
    url=models.SlugField(max_length=1000,unique=True)
    name=models.CharField(max_length=1000)
    desc=models.TextField()
    price_off=models.CharField(max_length=100)
    coupon=models.CharField(max_length=50,default='COUPON')
    date=models.DateTimeField(default=timezone.now)
    expired=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
  


SIZE_CHOICES = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    )    
class Product(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    
    url=models.SlugField(max_length=100,unique=True)
    name=models.CharField(max_length=100)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    image=models.ImageField(upload_to='static/images')
    image_1=models.ImageField(upload_to='static/images',blank=True)
    image_2=models.ImageField(upload_to='static/images',blank=True)
    image_3=models.ImageField(upload_to='static/images',blank=True)
    image_4=models.ImageField(upload_to='static/images',blank=True)
    size= models.CharField(max_length=10,choices=SIZE_CHOICES,default='M')
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE,blank=True)
    color=models.CharField(default='White',max_length=100)
    type=models.CharField(default='Regular',max_length=100)
    brand=models.CharField(default='Amazon',max_length=100)
    material=models.CharField(default='Cotton,Jeans',max_length=100)
    body=RichTextUploadingField()
    description=models.CharField(max_length=200)
    quantity=models.IntegerField(default=1)
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE,blank=True,null=True)
    warranty_info=models.TextField(default='This is product warranty info.')
    shipping_info=models.TextField(default='This is product shipping info.')
    tags=TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    def __str___(self):
        return self.offer.name,self.category
    

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(blank=True)
    phone=models.CharField(max_length=100,blank=True)
    city=models.CharField(max_length=100,blank=True)
    state=models.CharField(max_length=100,blank=True)
    zip=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.address
    
class Order(models.Model):
    order_id=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100,default='')
    signature=models.CharField(max_length=100,default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.CharField(max_length=100)
    product_id=models.IntegerField()
    price=models.BigIntegerField()
    quantity=models.IntegerField()
    total=models.BigIntegerField()
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.product

    
    

    

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products')
    rating=models.IntegerField(default=0)
    def __str___(self):
        return self.user
    



    



    

