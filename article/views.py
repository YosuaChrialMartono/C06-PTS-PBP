import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from article.models import ArticleForm, ArticlePage

def show_main_page(request):
    '''
    Show artikel tanpa login
    '''
    articles = ArticlePage.objects.all()
    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    p = Paginator(articles, 12)
    page_range = p.page_range

    try:
        page = p.page(page_num)
    except EmptyPage:
        page_num = 1


    last_page = 0
    for i in page_range:
        last_page = i
    context = {
        'page_num' : page_num,
        'page_range' : last_page
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


def show_json_by_page(request, page_num = 1):
    articles = ArticlePage.objects.all()

    p = Paginator(articles, 12)
    page = p.page(page_num)

    return HttpResponse(serializers.serialize("json", page), content_type="application/json")


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
        article_form = form.save(commit=False)
        article_form.author = request.user
        article_form.save()
        messages.success(request, 'Artikel telah berhasil dibuat!')
        return redirect('/article/')
    response = {'form': form}
    return render(request, 'form_article.html', response)


def save_article(request):
    form = ArticleForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
