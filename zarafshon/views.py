import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import login, logout

from django.contrib import messages
from django.views.generic import ListView, View
from zarafshon.models import Post, Tag
from zarafshon.forms import MessagesForm, LoginForm, SignUpForm

class homePageView(ListView):

    def get(self, request):
        posts = Post.objects.all()
        tags = Tag.objects.all()
        
        #eng so'nggi qo'wilgan post
        last_post = Post.objects.first
        video_tags = Post.objects.filter(type="Video")
        
        #gradus olish uchun
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Zarafshon'
        r = requests.get(url.format(city)).json()

        context = {'posts':posts, 'tags':tags, 'temperature': r["main"]["temp"], 
        'city':city, 'last_post':last_post, 'video_tags':video_tags}

        return render(request, 'index.html', context)

class TagPageView(View):


    def get(self, request, slug):
        posts = Post.objects.all()
        last_post = Post.objects.first
        video_tags = Post.objects.filter(type="Video")
        tags = Tag.objects.all()
        tag = Tag.objects.get(name=slug)
        
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Zarafshon'
        r = requests.get(url.format(city)).json()
        if tag:
            filter_posts = Post.objects.filter(tags=tag)
            return render(request, 'tags.html', context={'posts': posts,'filter_posts':filter_posts, 
            'temperature': r["main"]["temp"], 'city':city, 'tag': tag, 'tags':tags,'last_post':last_post,'video_tags':video_tags })
        return redirect('zarafshon:home')


class AboutUsView(ListView):

    def get(self, request):
        posts = Post.objects.all()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Zarafshon'
        r = requests.get(url.format(city)).json()
        context = {'posts':posts, 'temperature': r["main"]["temp"], 'city':city,}

        return render(request, 'pages/aboutus.html', context)


class ContactUsView(ListView):

    def get(self, request):
        posts = Post.objects.all()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Zarafshon'
        r = requests.get(url.format(city)).json()

        form = MessagesForm()
        context = {'posts':posts, 'temperature': r["main"]["temp"], 'city':city, 'form':form}
        return render(request, 'pages/contactus.html', context)


    def post(self, request):

        posts = Post.objects.all()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Zarafshon'
        r = requests.get(url.format(city)).json()
        form = MessagesForm(data=request.POST)
        context = {'posts':posts, 'temperature': r["main"]["temp"], 'city':city, 'form':form}   
        if form.is_valid():

            form.save()
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi')
            return redirect('zarafshon:home')

        return render(request, 'pages/contactus.html', context)



class NewsView(ListView):

    def get(self, request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Zarafshon'
        r = requests.get(url.format(city)).json()
        posts = Post.objects.all()
        news = Post.objects.filter(type='News')
        maqolas = Post.objects.filter(type="Maqola")
        context = {'posts':posts, 'news':news, 'maqolas':maqolas, 'temperature': r["main"]["temp"], 'city':city,}

        return render(request, 'pages/news.html', context)


class PostDetailPageView(View):


     def get(self, request, slug):

        posts = Post.objects.filter(type='News')
        post = Post.objects.get(slug=slug)
        context = {'posts':posts, 'post':post}
        return render(request, 'detail.html', context)


class Register(View):

    def get(self, request):
        form = SignUpForm()

        return render(request, 'register.html', {'form':form})

    def post(self, request):

        form = SignUpForm(request.POST)
        if form.is_valid():
            
            form.save()
            return  redirect('zarafshon:login')


        return render(request, 'register.html', {'form':form})



class Login(View):

    def get(self, request):
        login_form = LoginForm()

        return render(request, 'login.html', {'login_form':login_form})        

    def post(self, request):

        login_form = LoginForm(data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = User.objects.get(username=username)
            login(request, user)
            messages.success(request, f'Hurmatli <<{user.username}>> Muvaffaqiyatli Loginni amalga oshirdingiz ')
            return redirect('zarafshon:home')
        else:
            return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
   
    logout(request)
    return redirect("zarafshon:home")