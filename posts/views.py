from django.http import Http404
from django.shortcuts import render_to_response
from posts.models import Post

def index(request):
    posts = Post.objects.all()
    return render_to_response('posts/index.html', {
        'user': request.user,
        'posts': posts
    })

def show(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except:
        raise Http404('Requested Post Not Found')
    return render_to_response('posts/show.html', {
        'user' : request.user,
        'post' : post
    })