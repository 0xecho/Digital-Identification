from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as _logout
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.db.models import Q
import json
from cv import detect_face
# Create your views here.
class ImageUploadForm(forms.Form):
    image=forms.ImageField()

def createUser(request):
    context={
            "displacement_reason":Displacement.objects.all(),
            "disabilities":Disability.objects.all(),
            "country_of_origin":Country.objects.all(),
            "family":Family.objects.all(),
            }
    if request.method=='POST':
        if detect_face(request.FILES["img"]):
            l=Beneficiary()
            l.first_name=request.POST['first_name']
            l.last_name=request.POST['last_name']
            l.gender=Gender.objects.get(gender=request.POST['gender'])
            l.date_of_birth=request.POST['age']
            l.displacement_reason=Displacement.objects.get(pk=request.POST['displacement_reason'])
            try:
                l.disabilities=Disability.objects.get(pk=request.POST['disabilities'])
            except:
                pass
            l.country_of_origin=Country.objects.get(pk=request.POST['country_of_origin'])
            l.family=Family.objects.get(pk=request.POST['family'])
            l.family_role=request.POST['family_role']
            l.number_of_familymembers=len(l.family.beneficiary_set.all())+1
            form=ImageUploadForm(request.POST,request.FILES)
            print(form)
            if form.is_valid():
                l.photo=form.cleaned_data['img']
            l.save()
            context['error']=request.POST['first_name']+" "+request.POST['last_name']+" registered."
        else:
            context['error']="PHOTO HAS NO FACE, PLEASE RETAKE PHOTO"
    return render(request,'signup.html',context=context)
def add_family(request):
    f=Family()
    f.family=f.id
    f.save()
    # return render(request,'add_family.html',context=context)
    return redirect('signup')
def account(request):
    context={}
    print(request.FILES)
    if request.method=="POST":
        if detect_face(request.FILES["img"]):
            print("yes")
        else:
            print("no")
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
