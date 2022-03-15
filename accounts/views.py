from django.shortcuts import render,redirect
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request):
        title = "Welcome to best online job portal"
        context = {'title': title}
        return render(request,'common/index.html',context)


class Login(View):
    def get(self, request):
        title = "Login"
        context = {'title': title}
        return render(request,'common/login.html',context)
