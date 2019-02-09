from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.
# def userDir(instance,filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class Gender(models.Model):
    gender=models.CharField(max_length=50)
class Country(models.Model):
    country_of_origin=models.CharField(max_length=50,choices=tuple(json.load(open("out.json"))))
class Displacement(models.Model):
    displacement_reason=models.CharField(max_length=50,choices=(('r1','reason1'),('r2','reason2')))

class Disability(models.Model):
    disabilities=models.CharField(max_length=50,choices=(('blind','Visual Impairment'),('deaf','Hearing Impairment'),('mute','Speech Impairment'),('amputee','Amputee')))

class Beneficiary(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='beneficiary',null=True)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    date_of_birth=models.DateField()
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    displacement_reason=models.ForeignKey(Displacement,on_delete=models.CASCADE)
    number_of_familymembers=models.PositiveIntegerField() #Calculate
    disabilities=models.ForeignKey(Disability,on_delete=models.CASCADE)
    country_of_origin=models.ForeignKey(Country,on_delete=models.CASCADE)
    photo=models.CharField(max_length=255,default='Images/def.jpeg')
    #BIO METRIC SHIT
    def __str__(self):
        return self.user.username
    # def age

class Image(models.Model):
    img=models.CharField(max_length=255,null=True)
    uploader=models.ForeignKey(Beneficiary,on_delete=models.CASCADE,null=True,related_name='img')

# DO DIZ
# g=Gender()
# g.gender="male"
# g.save()
# g=Gender()
# g.gender="female"
# g.save()
