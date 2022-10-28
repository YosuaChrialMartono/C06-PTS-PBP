import datetime
from turtle import title
from django.shortcuts import render
from article.models import ArticleForm, ArticlePage
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def show_main_page(request):
    '''
    Show artikel tanpa login
    '''
    articles = ArticlePage.objects.all()
    context = {
        'article' : articles,
    }
    return render(request, "main_page.html", context)

def show_article_by_page(request, id):
    '''
    Show sebuah artikel khusus berdasarkan judul yang diberikan
    '''
    # Membuat id menjadi title yang dapat difilter
    id = id.replace("-", " ")

    article = ArticlePage.objects.filter(title = id)
    context = {
        'article' : article,
        'title' : id,
    }
    return render(request, "article_page.html", context)


def show_json(request):
    articles = ArticlePage.objects.all()
    return HttpResponse(serializers.serialize("json", articles), content_type="application/json")


def show_json_by_title(request, title):
    title = title.replace("-", " ")
    articles = ArticlePage.objects.all()
    filtered_article = []
    for article in articles:
        if article.title == title:
            filtered_article.append(article)
    # Jika JSON
    return HttpResponse(serializers.serialize("json", filtered_article), content_type="application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('article:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            # membuat response
            response = HttpResponseRedirect(reverse("article:show_main_page"))
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('article:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/article/login/')
def post_article(request):
    form = ArticleForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        new_article = form.save(commit=False)
        new_article.author = request.user
        new_article.save()
        return redirect('/article/')
    response = {'form': ArticleForm}
    return render(request, 'form_article.html', response)


def save_article(request):
    form = ArticleForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
