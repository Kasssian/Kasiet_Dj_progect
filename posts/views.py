from datetime import datetime

from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse(f'Hello {request.user}! Its my project')


def good_bay(request):
    #kasiet
    return HttpResponse(f'Good bay {request.user}!')


def now_date(request):
    return HttpResponse(datetime.now().date())


