from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from .models import *
# Create your views here.


class Index(View):
    def get(self, request):
        title = "Welcome to best online job portal"
        context = {'title': title}
        return render(request,'common/index.html',context)


class Login(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('dash')
        else:
            title = "Login"
            context = {'title': title}
            return render(request,'common/login.html',context)
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            msg = "Invalid User Credentials"
            title = "Invalid Login"
            return render(request,'common/login.html',{'msg':msg,'title':title})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class Dashboard(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
                if profile.type=='Admin':
                    return HttpResponse("Admin Dashboard")
                elif profile.type== 'AdminTeam':
                    return HttpResponse("AdminTeam Dashboard")
                elif profile.type== 'Employer':
                    return HttpResponse("Employer Dashboard")
                elif profile.type== 'EmployerTeam':
                    return HttpResponse("EmployerTeam Dashboard")
                elif profile.type== 'Candidate':
                    return HttpResponse("Candidate Dashboard")
                else:
                    return HttpResponse("User Profile Type not set")
            except:
                return HttpResponse("User Profile Type not set")
        else:
            return redirect('home')
            
