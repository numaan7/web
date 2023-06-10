from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','url')
    search_fields = ('name', 'url')
    prepopulated_fields = {'url': ('name',)}
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'url': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


admin.site.register(Newsletter)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name', 'email','message')
  
    date_hierarchy = 'date'
    ordering = ('date','name','email')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date',)
    search_fields = ('user', 'desc','quotes')
    date_hierarchy = 'date'
    raw_id_fields = ('user',)
    ordering = ('date','user','desc')
    list_filter = ('date', 'user', 'desc', 'quotes')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','date',)
    search_fields = ('user', 'comment','post')
    date_hierarchy = 'date'
    raw_id_fields = ('user',)
    ordering = ('date','user','post')
    list_filter = ('date', 'user', 'comment', 'post')

    