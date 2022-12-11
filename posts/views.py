from datetime import datetime

from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse(f'Hello {request.user}! Its my project')


def good_bay(request):
    return HttpResponse(f'<h1 style="color:red; text-align:center;font-size:500%;font-family: sans-serif";">Good bay {request.user}!</h1>')


def now_date(request):
    return HttpResponse(datetime.now().date())


