from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentForm


def accueil(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/accueil.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(id_post = id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.id_post = Post.objects.get(pk=id)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()

    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments' : comments})



def post_add(request, id=None):
        
    try:
        post=Post.objects.get(pk=id)
        first=False
    except Post.DoesNotExist:
        post=None
        first=True
    
    if request.method == "POST":
        
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        
            return render(request, 'blog/accueil.html', {'posts': posts})
    else:
            form = PostForm(instance = post)
            
    return render(request, 'blog/post_add.html', {'form': form, 'id':id})

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(id_post = id)
    
    if request.method == "POST":
        
        post.delete()
        comments.delete()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

        return render(request, 'blog/accueil.html', {'posts': posts})
    
    else:
        
        return render(request, 'blog/post_delete.html', {'post': post})