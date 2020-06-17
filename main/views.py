from django.http import HttpResponse

from .models import Post

def health_check(req):
    # TODO: connect to db

    return HttpResponse('OK')


def home(req):
    p = Post.objects.all()[0]

    return HttpResponse(p.content, content_type='text/plain')
