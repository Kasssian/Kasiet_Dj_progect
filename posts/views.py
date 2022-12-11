from datetime import datetime

from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse('Hello! Its my project')


def good_bay(request):
    return HttpResponse(f'<h1>Good bay {request.user}!</h1>')


def now_date(request):
    return HttpResponse(datetime.now().date())


