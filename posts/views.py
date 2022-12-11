from datetime import datetime

from django.shortcuts import HttpResponse


def hello(requests):
    return HttpResponse('Hello! Its my project')


def good_bay(requests):
    return HttpResponse(f'<h1>Good bay {requests.user}!</h1>')


def now_date(requests):
    return HttpResponse(datetime.now().date())


