from django.shortcuts import render,HttpResponse
# from django.contrib.auth.models import User
from .models import Page,Post,Song,User

# Create your views here.



def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email = 'csk@123.com')
    data3 = User.objects.filter(page__page_cat = 'fgdhfghfgd')
    data4 = User.objects.filter(post__post_publish_date = '2023-09-12')
    data5 = User.objects.filter(song__song_duration = 3)
    return render(request,'home.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})

def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat = 'fgdhfghfgd')
    data3 = Page.objects.filter(user__username = 'ajay')
    return render(request,'page.html',{'data1':data1,'data2':data2,'data3':data3})

def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_publish_date = '2023-09-12')
    data3 = Post.objects.filter(user__username = 'ajay')
    
    return render(request,'post.html',{'data1':data1,'data2':data2,'data3':data3})

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration = 3)
    data3 = Song.objects.filter(user__username = 'ajay')
    return render(request,'song.html',{'data1':data1,'data2':data2,'data3':data3})
