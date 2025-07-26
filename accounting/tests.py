from django.test import TestCase

def say_hello(request):
    return HttpResponse ("Hello")
