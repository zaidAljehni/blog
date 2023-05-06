from datetime import date

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import lorem_ipsum

posts = [
    {
        "title": "title-1",
        "author": "Franz",
        "excerpt": lorem_ipsum.paragraph(),
        "content": lorem_ipsum.paragraph(),
        "slug": "post-1",
        "date": date(2023, 5, 3),
        "image": "mountains.jpg",
    },
    {
        "title": "title-2",
        "author": "Antoine",
        "excerpt": lorem_ipsum.paragraph(),
        "content": lorem_ipsum.paragraph(),
        "slug": "post-2",
        "date": date(2023, 5, 2),
        "image": "woods.jpg",
    },
    {
        "title": "title-3",
        "author": "Jad",
        "excerpt": lorem_ipsum.paragraph(),
        "content": lorem_ipsum.paragraph(),
        "slug": "post-3",
        "date": date(2023, 4, 1),
        "image": "coding.jpg",
    },
]


# Create your views here.
def home(request):
    return render(request, "posts/home.html", {
        "posts": sorted(
            posts,
            reverse=True,
            key=lambda post: post.get("date")
        )[:2]
    })


def index(request):
    return render(request, "posts/index.html", {
        "posts": sorted(
            posts,
            reverse=True,
            key=lambda post: post.get("date")
        )
    })


def view(request, slug):
    responsePost = None
    for post in posts:
        if post.get("slug", None) == slug:
            responsePost = post
            break

    if responsePost == None:
        return HttpResponseNotFound("404")

    return render(request, "posts/view.html", {
        "post": responsePost
    })
