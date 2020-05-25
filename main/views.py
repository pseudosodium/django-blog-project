from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import blog, blogCategory, blogSeries
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.models import User

def single_slug(request, single_slug):
    categories = [c.category_slug for c in blogCategory.objects.all()]

    if single_slug in categories:
        matching_series = blogSeries.objects.filter(blog_category__category_slug=single_slug)
        series_url = {}

        for m in matching_series.all():
            part_one = blog.objects.filter(blog_series__blog_series=m.blog_series).earliest("blog_publishedDate")
            series_url[m] = part_one.blog_slug

        return render(request, "main/category.html", context={"blog_series":matching_series, "part_ones":series_url})

    blogs = [t.blog_slug for t in blog.objects.all()]
    if single_slug in blogs:
        this_blog = blog.objects.get(blog_slug=single_slug)
        blogs_from_series = blog.objects.filter(blog_series__blog_series=this_blog.blog_series).order_by("blog_publishedDate")
        this_blog_idx = list(blogs_from_series).index(this_blog)
        return render(request, "main/blog.html", {"blog":this_blog, "sidebar":blogs_from_series, "this_blog_idx":this_blog_idx})

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")


def account(request):
    return render(request, 'main/account.html', {"user":request.user})

def homepage(request):
    return render(request=request,
                    template_name="main/categories.html",
                    context={"categories":blogCategory.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Acccount Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form":form})
