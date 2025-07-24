from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import BlogForms
from blog.models import Blog

@login_required
def home(request):
    blogs = Blog.objects.filter(published_at=True)
    search_published_blog = request.GET.get('search_published_blog')
    if search_published_blog:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_published_blog) | Q(content__icontains=search_published_blog), published_at=True)
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def create(request):
    if request.method == "POST":
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForms()

    context = {
        "form": form
    }
    return render(request, 'blog/create.html', context=context)