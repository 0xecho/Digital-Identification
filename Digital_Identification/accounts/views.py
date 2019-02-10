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
    posted=False
    if(request.method=='POST'):
        posted=True
        req=request.POST
        org=req["Orginization"]
        cit=req["citizen_info"]
        a=Orginization.objects.get(orginization=org)
        fn=a.first_name
        ln=a.last_name
        dob=a.date_of_birth
        gen=a.gender
        disr=a.displacement_reason
        dissa=a.disabilities
        coo=a.country_of_origin
        photo=a.photo
        arr=(fn,ln,dob,gen,disr,dissa,coo,photo)

        # TODO: check org;;;
        first_name=""
        last_name=""
        date_of_birth=""
        gender=""
        displacement_reason=""
        number_of_familymembers=""
        disabilities=""
        country_of_origin=""
        photo=""


        xx=Beneficiary.objects.get(pk=1)
        if(fn):
            first_name=xx.first_name;
        else:
            first_name="Not Available"
        if(ln):
            last_name=xx.last_name
        else:
            last_name="Not Available"
        if(dob):
            date_of_birth=xx.date_of_birth
        else:
            date_of_birth="Not Available"
        if(gen):
            gender=xx.gender
        else:
            gender="Not Available"
        if(disr):
            displacement_reason=xx.displacement_reason;
        else:
            displacement_reason="Not Available"
        if(dissa):
            disabilities=xx.disabilities
        else:
            disabilities="Not Available"
        if(coo):
            country_of_origin=xx.country_of_origin
        else:
            country_of_origin="Not Available"
        if(photo):
            photo=xx.photo
        else:
            photo="N"
        context={"p":posted,"fn":first_name,"ln":last_name,"dob":date_of_birth,"gen":gender,"disr":displacement_reason,"dissa":disabilities,"coo":country_of_origin,"photo":photo}

        return render(request,'Orginizations/Search_Personel.html',context)
    return render(request,'Orginizations/Search_Personel.html',{"p":posted})
##############################################33##############################################33##############################################33##############################################33##############################################33
# import the necessary packages
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2

def detect(request):
	# initialize the data dictionary to be returned by the request
	data = {"success": False}

	# check to see if this is a post request
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])

		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)

			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)

			# load the image and convert
			image = _grab_image(url=url)

		### START WRAPPING OF COMPUTER VISION APP
		# Insert code here to process the image and update
		# the `data` dictionary with your results
		### END WRAPPING OF COMPUTER VISION APP

		# update the data dictionary
		data["success"] = True

	# return a JSON response
	return JsonResponse(data)

def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)

	# otherwise, the image does not reside on disk
	else:
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()

		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()

		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# return the image
	return image
