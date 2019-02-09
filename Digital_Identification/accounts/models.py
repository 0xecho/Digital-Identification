from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.
# def userDir(instance,filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)
Id_type = ("CIT","REF")
class Beneficiary(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=50,choices=(('male','male'),('female','female')))
    displacement_reason=models.CharField(max_length=50,choices=(('r1','reason1'),('r2','reason2')))
    number_of_familymembers=models.PositiveIntegerField()
    disabilities=models.CharField(max_length=50,choices=(('blind','Visual Impairment'),('deaf','Hearing Impairment'),('mute','Speech Impairment'),('amputee','Amputee')))
    country_of_origin=models.CharField(max_length=50,choices=tuple(json.load(open("out.json"))))
    photo=models.CharField(max_length=255,default='Images/def.jpeg')
    Registerd_By=models.ForeignKey(User,on_delete=models.CASCADE,related_name='beneficiary',null=True)
    Registerd_On=models.DateTimeField(auto_now_add=True,null=True)
    Person_Id=models.CharField(max_length=255,null=True,unique=True)
    def __str__(self):
        return self.first_name

class Image(models.Model):
    img=models.CharField(max_length=255,null=True)
    uploader=models.ForeignKey(Beneficiary,on_delete=models.CASCADE,null=True,related_name='img')
class Orginization(models.Model):
    orginization=models.CharField(max_length=255,null=True)
    first_name=models.BooleanField()
    last_name=models.BooleanField()
    date_of_birth=models.BooleanField()
    gender=models.BooleanField()
    displacement_reason=models.BooleanField()
    number_of_familymembers=models.BooleanField()
    disabilities=models.BooleanField()
    country_of_origin=models.BooleanField()
    photo=models.BooleanField()
    def __str__(self):
        return self.orginization
