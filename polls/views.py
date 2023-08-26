from django.http import HttpResponse


def index(request, year=''):
    return HttpResponse(f"<h1>hello, world. you're at the polls index. Year: {year}!</h1>")
