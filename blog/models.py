from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email_address= models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.Slugfield(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts") 
    # related name is used to access the posts of an author
    # on_delete=models.SET_NULL means that if the author is deleted, the post will still exist but the author will be null 
    # null=True means that the author can be null
    # db_index=True means that the slug will be indexed in the database for faster lookup
    # author is a foreign key to the Author model
    # author field is related to Author model as one to many relationship
    # author is the parent and post is the child