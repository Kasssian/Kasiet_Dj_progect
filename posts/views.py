from datetime import datetime
from posts.models import Post
from django.shortcuts import HttpResponse, render


def hello(request):
    return HttpResponse(f'Hello {request.user}! Its my project')


def good_bay(request):
    return HttpResponse(f'Good bay {request.user}!')


def now_date(request):
    return HttpResponse(datetime.now().date())


def rend(request):
    return render(request, 'layouts/index.html')


def img(request):
    return HttpResponse(img('DjangoProject/hq720_1.jpg'))


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        print(posts)
        return render(request, 'posts/posts.html', context={
            'posts': posts
        })
