from django.shortcuts import render,redirect
from django.db import models
from .forms import PostForm
from .models import Post
from  accounts.models import Author
from django.views.generic import (
    ListView
)


def home_page(request):
    return render(request, 'pinterest/home_page.html')
class TitleDescriptionResulsView(ListView):
    model = Post
    template_name = 'main/search.html'
def post_list(request):
    posts = Post.objects.all()
    accounts = Author.objects.all()
    context = {
        'posts': posts,
        'accounts': accounts  
    }

    return render(request,'pinterest/post_list.html',context=context)
def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    context = {'post' : post }
    return render(request,'pinterest/detail_post.html',context = context)
def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('post_list')

    context = {
        'form': form
    }

    return render(request, 'pinterest/detail_create.html', context=context)





def post_edit(request, pk):
    instance = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = PostForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'pinterest/detail_edit.html', context=context)
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    
    return redirect('post_list')
def my_post(request):
    if request.user.is_authenticated:
        post = Post.objects.filter(author=request.user)
        context = {
            'post': post
        }
        return render(request, 'pinterest/my_posts.html', context=context)
    else:
        return render(request, 'pinterest/my_posts.html')  

def signup(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Assuming you have a 'login' URL name
    else:
        form = ()
    return render(request,'registration/signup.html', {'form': form})
def LoginPage(request):
    return render(request,'registration/login.html')


class Pin(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()



