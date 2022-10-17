from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():

            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all()[:20]
    #show
    return render(request, 'posts.html',
                    {'posts': posts})


def delete(request, post_id):
    #find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form=PostForm
    return render(request, 'edit.html', {'post': post, 'form':form})


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.like_count == 0:
        post.like_count += 1
        post.save()
    else:
        post.like_count = 0
        post.save()
    return HttpResponseRedirect('/')

def cancel(request, post_id):
    return HttpResponseRedirect('/')