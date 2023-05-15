from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'url': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','url')
    
    search_fields = ('name', 'url')
    prepopulated_fields = {'url': ('name',)}
admin.site.register(Newsletter)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name', 'email','message')
  
    date_hierarchy = 'date'
    ordering = ('date','name','email')

admin.site.register(Profile)
  

    