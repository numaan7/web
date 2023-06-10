from django.contrib import admin
from . models import *
from blog.models import Categorie
# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price_off')
    list_filter = ('price_off', 'name')
    search_fields = ('name', 'price_off')
    prepopulated_fields = {'url': ('name',)}
    ordering = ('price_off', )
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'publish', 'quantity')
    list_filter = ('status', 'created', 'publish', 'price')
    search_fields = ('name', 'body')
    prepopulated_fields = {'url': ('name',)}
    raw_id_fields = ('seller',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
   
    prepopulated_fields = {'url': ('name',)}
   

admin.site.register(Address)
admin.site.register(Rating)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at', 'total', 'order_id', 'paid')
    list_filter = ('created_at', 'paid', )
    search_fields = ('order_id', 'signature','payment_id')
    
    date_hierarchy = 'created_at'
    ordering = ('paid', 'created_at')
  
