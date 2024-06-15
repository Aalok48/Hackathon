from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def user_login(request):
    return HttpResponse('Hello there this is login page')

def user_signup(request):
    return HttpResponse('Hello there this is signup page')