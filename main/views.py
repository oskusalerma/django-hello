from django.http import HttpResponse

def health_check(req):
    # TODO: connect to db

    return HttpResponse('OK')


def home(req):
    # TODO: read response from db

    return HttpResponse('I am groot')
