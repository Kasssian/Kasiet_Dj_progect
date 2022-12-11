from datetime import datetime

from django.shortcuts import HttpResponse


def hello(requests):
    return HttpResponse('Hello! Its my project')


def good_bay(requests):
    return HttpResponse('Good bay user!')


def now_date(requests):
    return HttpResponse(datetime.now().date())
