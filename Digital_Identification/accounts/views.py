from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as _logout
from django.contrib.auth.models import User
from .models import Beneficiary
from django.db.models import Q
# Create your views here.

def createUser(request):
    context={}
    if request.method=='POST':
        print(request.POST)
        if not request.POST['password'] == request.POST['password2'] :
            context['error']="passwords doesn't match please try again"
            return render(request,'signup.html',context=context)
        try:
            User.objects.get(username=request.POST['username'])
            context['error']="Username Already taken"
            return render(request,'signup.html',context=context)
        except User.DoesNotExist:
            pass
        l=Beneficiary()
        l.first_name=request.POST['first_name']
        l.last_name=request.POST['last_name']
        l.age=request.POST['age']
        l.gender=request.POST['gender']
        u=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
        l.user=u
        l.save()
        u=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        login(request,u)
        return redirect('account')
    return render(request,'signup.html',context=context)
def account(request):
    context={}
    return render(request,'account.html',context=context)
def profile(request):
    context={}
    try:
        print(request.GET['uid'])
        if not request.GET['uid'] is None:
            context['uid']=request.GET['uid']
            context['user']=User.objects.get(pk=context['uid'])
    except:
        pass
    print(context)
    return render(request,'profile.html',context=context)
def logout(request):
    context={}
    _logout(request)
    return redirect('account')
def search(request):
    context={}
    if request.method=='GET':
        t=request.GET['term']
        try:
            context['users']=User.objects.filter(Q(username__icontains=t)|Q(first_name__icontains=t)|Q(last_name__icontains=t))
        except:
            pass
    return render(request,'search.html',context=context)
def settings(request):
    context={}
    if request.method=='POST':
        print(request.POST)
    return render(request,'settings.html',context=context)

def search(request):
    return render(request,'Orginizations/Search_Personel.html')
