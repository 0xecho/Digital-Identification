from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.
# def userDir(instance,filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class Gender(models.Model):
    gender=models.CharField(max_length=50)

class Country(models.Model):
    country_of_origin=models.CharField(max_length=50)
if len(Country.objects.all())==0:
    for i,j in json.load(open("out.json")):
        c=Country()
        c.country_of_origin=j
        c.save()

class Displacement(models.Model):
    displacement_reason=models.CharField(max_length=50,choices=(('r1','reason1'),('r2','reason2')))

class Family(models.Model):
    family=models.CharField(max_length=50)
    # number_of_familymembers=models.PositiveIntegerField() #Calculate
    def number_of_familymembers():
        return len(self.objects.all())
    def __str__(self):
        return self.family
class Disability(models.Model):
    disabilities=models.CharField(max_length=50,
                                choices=(('blind','Visual Impairment'),
                                ('deaf','Hearing Impairment'),
                                ('mute','Speech Impairment'),
                                ('amputee','Amputee')))
    def __str__(self):
        return self.disabilities

class Beneficiary(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='beneficiary',null=True)
    first_name=models.CharField(max_length=50,default="NaN")
    last_name=models.CharField(max_length=50,null=True)
    date_of_birth=models.DateField()
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    displacement_reason=models.ForeignKey(Displacement,on_delete=models.CASCADE)
    disabilities=models.ForeignKey(Disability,on_delete=models.CASCADE,null=True)
    country_of_origin=models.ForeignKey(Country,on_delete=models.CASCADE)
    family_role=models.CharField(max_length=50,choices=(("m","Mother"),("f","Father"),("c","Child")),null=True)
    family=models.ForeignKey(Family,on_delete=models.CASCADE,null=True)
    photo=models.ImageField(upload_to="Uploads/",default='Images/def.jpeg')
    #BIO METRIC SHIT
    def __str__(self):
        return self.first_name
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
