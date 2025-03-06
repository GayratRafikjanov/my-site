from django.contrib import admin
from .models import Author, Post, Tag   # import the models from models.py
# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)