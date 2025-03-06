from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)


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
    # related name is used to access the posts of an author
    # on_delete=models.SET_NULL means that if the author is deleted, the post will still exist but the author will be null 
    # null=True means that the author can be null
    # db_index=True means that the slug will be indexed in the database for faster lookup
    # author is a foreign key to the Author model
    # author field is related to Author model as many to one relationship
    # The author field in the Post model is a foreign key that creates a many-to-one relationship with the Author model. 
    # This means each post is associated with one author, but an author can have multiple posts.
    # author is the parent and post is the child
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    # tags is a many to many relationship with the Tag model 
    tags = models.ManyToManyField(Tag)