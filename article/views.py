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
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from django.db.utils import OperationalError


from article.models import ArticleForm, ArticlesPage

def show_main_page(request):
    '''
    Show artikel tanpa login
    '''
    articles = ArticlesPage.objects.all()
    page_num = request.GET.get('page', 1)
    p = Paginator(articles, 12)

    try:
        page_range = p.page_range
        page_num = int(page_num)
        page = p.page(page_num)
        last_page = 0
        for i in page_range:
            last_page = i
    except EmptyPage:
        page_num = 1
    
    except OperationalError:
        page_range = 0
        page_num = 0
        last_page = 0
    if request.user.username == '':
            role = "PENGUNJUNG"
    else:
            role = request.user.role
    context = {
        'page_num' : page_num,
        'page_range' : last_page,
        'role' : role,
    }
    return render(request, "main_page.html", context)

def show_article_by_page(request, id):
    '''
    Show sebuah artikel khusus berdasarkan judul yang diberikan
    '''
    # Membuat id menjadi title yang dapat difilter
    id = id.replace("-", " ")

    article = ArticlesPage.objects.filter(title = id)
    context = {
        'article' : article,
        'title' : id,
    }
    return render(request, "article_page.html", context)


def show_json(request):
    articles = ArticlesPage.objects.all()

    return HttpResponse(serializers.serialize("json", articles), content_type="application/json")


def show_json_by_page(request, page_num = 1):
    articles = ArticlesPage.objects.all()

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
        return redirect('/article/')
    response = {'form': form}
    return render(request, 'form_article.html', response)

@csrf_exempt
def post_article_flutter(request):
    if (request.method == 'POST'):
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            article_form = form.save(commit=False)
            article_form.author = request.user.username
            article_form.save()
            return JsonResponse({
              "status": True,
              "message": "Berhasil post artikel",
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
    return JsonResponse({
              "status": False,
              "message": form.errors,
              # Insert any extra data if you want to pass data to Flutter
            }, status=401)

def save_article(request):
    form = ArticleForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
