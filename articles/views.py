from articles import models
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout


def archive(request):
    return render(request, 'archive.html', {"posts": models.Article.objects.all()})


def get_article(request, article_id):
    try:
        post = models.Article.objects.get(id=article_id)
        return render(request, f'article.html', {"post": post})
    except models.Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not(request.user.is_anonymous):
        if request.method == "POST":
        # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
        # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
        # если поля заполнены без ошибок
                if models.Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Такая запись уже существует"
                    return render(request, 'create_post.html', {'form': form})
                article = models.Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
        # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
 
    else:
        raise Http404

    
def registrate(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'username': request.POST["username"], 'password': request.POST["password"], 'email': request.POST["email"]
        }
        username = form["username"]
        password = form["password"]
        email = form["email"]
        try:
            User.objects.get(username=username)
            # если пользователь существует, то ошибки не произойдет и программа # удачно доберется до следующей строчки 
            form['errors'] = u"Пользователь с таким именем уже есть!"
            return render (request, 'registration.html', {'form': form})
        except User.DoesNotExist:
            User.objects.create_user(username, email, password)
            return redirect('archive')
        return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 'password': request.POST["password"]
        }
        username = form["username"]
        password = form["password"]

        user = authenticate(username = username, password = password)

        if user != None:
            dj_login(request, user)
            return redirect('archive')
        else:
            form['errors'] = u"Неправильный логин или пароль!"
            return render(request, 'login.html', {'form': form})
    else:
        if not(request.user.is_anonymous):
            return redirect('archive')
        return render(request, 'login.html')

def exit(request):
    logout(request)
    return redirect('archive')
