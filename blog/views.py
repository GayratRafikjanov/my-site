from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post
# Create your views here.


all_posts = []

def get_date(post):
    return post['date'] # get the date of the post

def starting_page(request):
    lastest_posts = Post.objects.all().order_by('-date')[:3] # get the lastest 3 posts
    return render(request, "blog/index.html", { # render the index.html template
        "posts": lastest_posts # pass the lastest 3 posts to the template
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date') # get all the posts and order them by date
    return render (request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug) # get the post with the slug
    return render (request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all() # get all the tags of the post
    })