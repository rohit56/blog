from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from example.config import pagination
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('blog:post_list_admin'))
        else:
            context['error'] = 'Username or password is invalid !!!'
            return render(request, 'auth/login.html', context)
    else:
        return render(request, 'auth/login.html', context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))


@login_required(login_url='/login/')
def post_list(request):
    template = 'blog/post_list.html'
    object_list = Post.objects.filter(status='Published')

    pages = pagination(request, object_list, 1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def post_detail(request, slug):
    template = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def category_detail(request, slug):
    template = 'blog/category_detail.html'
    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category, status='Published')
    context = {
        'category': category,
        'post': post,
    }
    return render(request, template, context)

@login_required(login_url='/login/')
def search(request):
    template = 'blog/post_list.html'
    query = request.GET.get('q')

    if query:
        result = Post.objects.filter(Q(title__icontains=query))
    else:
        result = Post.objects.filter(status='Published')
    pages = pagination(request, result, num=1)
    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def new_post(request):
    template = 'blog/new_post.html'
    form = PostForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post was saved to the database')

    except Exception as e:
        messages.warning(request, 'Blog post was not saved. Error: {}'.format(e))
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required(login_url='/login/')
def edit_post(request, pk):
    template = 'blog/new_post.html'
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Blog post has been updated')
        except Exception as e:
            messages.warning(request, 'Your post was not saved do to an error:{}'.format(e))

    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def delete_post(request, pk):
    template = 'blog/new_post.html'
    post = get_object_or_404(Post, pk=pk)
    try:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            post.delete()
            messages.success(request, 'You have successfully deleted post')
        else:
            form = PostForm(instance=post)
    except Exception as e:
        messages.warning(request, 'The post could not be deleted. error:{}'.format(e))

    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def post_list_admin(request):
    template = 'blog/post_list_admin.html'
    post = Post.objects.all()
    pages = pagination(request, post, 3)
    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)



