from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.serializers import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, PostImage, comment
from .forms import AddUser
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.core import serializers


# ------PAGES-------
@login_required(login_url='/login/')
def basepage(request):
    return render(request, 'base.html')


def usersettings(request):
    return render(request, 'usersettings.html')


def mainpage(request):
    Posts = Post.objects.all()
    PostImages = PostImage.objects.all()
    return render(request, 'mainpage.html',
                  {'posts': Posts,
                   'PostImages': PostImages
                   })


def signuppage(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        messages.success(request, 'Account created successfully')
        form.save()
    context = {
        'form': form}
    return render(request, 'signup.html', context)


def loginpage(request):
    return render(request, 'login.html')


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    PostImages = PostImage.objects.all()
    comments = comment.objects.filter(post=post_id)
    return render(request, 'postdetail.html',
                  {'post': post,
                   'PostImages': PostImages,
                   'comments': comments
                   })

    # -----Authentication-------


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/mainpage/')
    else:
        return HttpResponseRedirect('/login/')


def logut(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def update_user(request):
    finded_user = User.objects.get(username=request.user)
    finded_user.first_name = request.POST.get('first_name')
    finded_user.last_name = request.POST.get('last_name')
    finded_user.save()
    return HttpResponseRedirect('/usersettings/')


def add_img(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    p = Post(author=request.user, title=title, description=description)
    p.save()
    photo = request.FILES['document']
    fs = FileSystemStorage()
    photo = fs.save(photo.name, photo)
    url = fs.url(photo)
    new_Postimage = PostImage(
        image=url,
        post=p
    )
    new_Postimage.save()
    return HttpResponseRedirect('/')


def add_comment(request, post_id):
    comment_for_post = request.POST.get('comment')
    commented_post = Post.objects.get(id=post_id)
    new_comment = comment(
        content=comment_for_post,
        post=commented_post,
        commentor=request.user
    )
    new_comment.save()
    return HttpResponseRedirect('/postdetail/' + str(post_id) + '/')

def delete_comment(request,comment_id):
    comment_for_delete = comment.objects.get(id=comment_id)
    comment_for_delete.delete()
    post = comment_for_delete.post.id
    return HttpResponseRedirect('/postdetail/' + str(post) + '/')



